import asyncio
import logging
from aiogram import Bot,Dispatcher
from app.handlers import router
import os
from dotenv import load_dotenv
from app.db import init_db

load_dotenv()
API_KEY = os.getenv("API_KEY")
bot = Bot(token=API_KEY)


dp = Dispatcher()



async def main():
    init_db()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')