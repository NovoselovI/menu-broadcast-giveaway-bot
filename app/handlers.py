import asyncio
import logging
import random

from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramForbiddenError, TelegramRetryAfter, TelegramBadRequest

from app.config_loader import config
from app.states import Broadcast
from app.db import (
    save_user, get_all_users, get_all_participants,
    save_participant,get_participant_full
)
import app.keyboards as kb
from app.keyboards import participate_keyboard

ADMIN_ID = 412718651



router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    save_user(
        user_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name
    )

    await message.answer_video(video="BAACAgIAAxkBAAODaRMHL1rq1K5IYXbi6gFcK4VrjCUAAt58AAKyEJhIVo1btZka3Hk2BA",caption=config["start_text"],reply_markup=kb.main)

@router.callback_query(F.data == 'legend')
async def legend(callback: CallbackQuery):
    await callback.answer('🎭Легенда гласит...')
    await callback.message.delete()
    await callback.message.answer(config["legend"], reply_markup=kb.main)

@router.callback_query(F.data == 'program')
async def program(callback: CallbackQuery):
    await callback.answer('Что тебя ждет...')
    await callback.message.delete()
    await callback.message.answer(config["program"],reply_markup=kb.main)

@router.callback_query(F.data == 'activities')
async def activities(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer('')
    await callback.message.answer(config["activities"],reply_markup=kb.activities)

@router.callback_query(F.data == 'contacts')
async def contact(callback: CallbackQuery):
    await callback.answer('👁️Ты найдёшь меня здесь ...')
    await callback.message.delete()
    await callback.message.answer(config["contacts"],reply_markup=kb.adress)
    
@router.callback_query(F.data == 'menu')
async def menu(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer('')
    await callback.message.answer(config["menu"],reply_markup=kb.main)
    
@router.callback_query(F.data == 'restraunts')
async def restraunts(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer('')
    await callback.message.answer(config["restraunts"],reply_markup=kb.back_activities)

@router.callback_query(F.data == 'animation')
async def animation(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer('')
    await callback.message.answer(config["animation"],reply_markup=kb.back_activities)
    
@router.callback_query(F.data == 'sales')
async def sales(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer('')
    await callback.message.answer(config["sales"],reply_markup=kb.back_activities)

@router.callback_query(F.data == 'back_activities')
async def back_activities(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer('')
    await callback.message.answer(config["activities"], reply_markup=kb.activities)


@router.callback_query(F.data == 'back')
async def back(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer('')
    await callback.message.answer(config["start_text"],reply_markup=kb.main)


@router.message(Command("broadcast"))
async def start_broadcast(message: Message, state: FSMContext):
    if message.from_user.id != ADMIN_ID:
        return await message.answer("❌ У вас нет прав на эту команду.")

    await message.answer("📨 Введите текст рассылки:")
    await state.set_state(Broadcast.waiting_for_text)




@router.message(Broadcast.waiting_for_text)
async def process_broadcast_text(message: Message, state: FSMContext):
    text = message.text
    user_ids = get_all_users()
    sent = 0
    failed = 0

    await message.answer(f"🚀 Начинаю рассылку для {len(user_ids)} пользователей...")

    for user_id in user_ids:
        try:
            await message.bot.send_message(user_id, text)
            sent += 1
            await asyncio.sleep(0.1)
        except TelegramForbiddenError:
            failed += 1
        except TelegramRetryAfter as e:
            await asyncio.sleep(e.retry_after)
            continue
        except TelegramBadRequest:
            failed += 1
        except Exception as e:
            logging.error(f"Ошибка при отправке {user_id}: {e}")
            failed += 1

    await message.answer(f"✅ Рассылка завершена\nУспешно: {sent}\nОшибки: {failed}")
    await state.clear()

@router.callback_query(F.data == "participate")
async def handle_participation(callback: CallbackQuery):
    save_participant(callback.from_user.id)
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.answer("✅ Вы зарегистрированы на розыгрыш!")

@router.message(Command("invite"))
async def invite_to_draw(message: Message):
    if message.from_user.id != ADMIN_ID:
        return await message.answer("❌ Нет доступа")

    users = get_all_users()
    sent = 0
    for user_id in users:
        try:
            await message.bot.send_message(
                user_id,
                "🎉 Примите участие в розыгрыше! Жмите кнопку ниже:",
                reply_markup=participate_keyboard
            )
            sent += 1
            await asyncio.sleep(0.1)
        except Exception:
            continue

    await message.answer(f"✅ Отправлено {sent} пользователям.")



@router.message(Command("draw"))
async def draw_winner(message: Message):
    if message.from_user.id != ADMIN_ID:
        return await message.answer("❌ Нет доступа")

    participants = get_all_participants()
    if not participants:
        return await message.answer("📭 Пока никто не участвует в розыгрыше.")

    winner_id = random.choice(participants)
    username, first_name = get_participant_full(winner_id) or ("❓", "Без имени")

    try:
        await message.bot.send_message(winner_id, "🎉 Поздравляем! Вы победили в розыгрыше!")
        await message.answer(
            f"🏆 Победитель:\nID: <code>{winner_id}</code>\nИмя: {first_name}\nUsername: @{username}",
            parse_mode="HTML"
        )
    except Exception as e:
        await message.answer(f"⚠️ Ошибка при отправке победителю ({winner_id}): {e}")
