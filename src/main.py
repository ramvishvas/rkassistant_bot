
import asyncio
from telegram_bot import TelegramBot
from env_handler import EnvHandler

# Configuration
TELEGRAM_BOT_TOKEN = EnvHandler().get_variable('TELEGRAM_BOT_TOKEN')
OPENAI_API_KEY = EnvHandler().get_variable('OPENAI_API_KEY')


async def main():
    """Main bot startup function"""
    print(TELEGRAM_BOT_TOKEN, OPENAI_API_KEY)

    bot = TelegramBot(TELEGRAM_BOT_TOKEN, OPENAI_API_KEY)
    await bot.start()

if __name__ == '__main__':
    asyncio.run(main())