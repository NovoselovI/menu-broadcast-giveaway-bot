from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)


from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🎭 Легенда", callback_data="legend"),
            InlineKeyboardButton(text="🗓 Программа", callback_data="program")
        ],
        [
            InlineKeyboardButton(text="🍽 Меню", callback_data="menu"),
            InlineKeyboardButton(text="🎉 Активности", callback_data="activities")
        ],
        [
            InlineKeyboardButton(text="📞 Контакты", callback_data="contacts")
        ]
    ]
)

adress = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📍 Яндекс.Карты", url='https://yandex.ru/maps/?pt=37.620070,55.753630&z=18&l=map'),
        InlineKeyboardButton(text="🔙 Назад", callback_data="back")
        ]
    ]
)

activities = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🍷Рестораны", callback_data="restraunts"),
            InlineKeyboardButton(text="🧸Анимация", callback_data="animation")
           
        ]
        
        ,[

            InlineKeyboardButton(text="🎁Акции", callback_data="sales"),
            InlineKeyboardButton(text="🔙 Назад", callback_data="back")
        ]
    ]
)
back_activities = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 Назад", callback_data="back_activities")
        ]
    ]
)
participate_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🎁 Участвовать", callback_data="participate")]
])