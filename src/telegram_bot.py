import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from ai_handler import AIHandler


class TelegramBot:
    def __init__(self, telegram_token: str, openai_api_key: str):
        """Initialize Telegram Bot with AI Handler"""
        self.bot = Bot(token=telegram_token)
        self.dp = Dispatcher()
        self.ai_handler = AIHandler(api_key=openai_api_key)
        self.user_conversations = {}

        # Register handlers
        self.dp.message(CommandStart())(self.handle_start)
        self.dp.message()(self.handle_message)

    async def handle_start(self, message: types.Message):
        """Handle bot start command"""
        await message.answer(
            "Welcome! I'm an AI assistant. Send me a message, and I'll help you out."
        )

    async def handle_message(self, message: types.Message):
        """Main message handler with AI response"""
        try:
            user_id = message.from_user.id

            system_prompt = "You are a helpful and friendly AI assistant."

            self.user_conversations.setdefault(user_id, [])
            self.user_conversations[user_id].append({"role": "user", "content": message.text})

            if len(self.user_conversations[user_id]) > 5:
                self.user_conversations[user_id] = self.user_conversations[user_id][-5:]

            ai_response = self.ai_handler.generate_contextual_response(
                conversation_history=self.user_conversations[user_id][:-1],
                user_message=message.text,
                system_prompt=system_prompt
            )

            self.user_conversations[user_id].append({"role": "assistant", "content": ai_response})

            await message.answer(ai_response)

        except Exception as e:
            await message.answer(f"An error occurred: {str(e)}")

    async def start(self):
        """Start bot polling"""
        logging.basicConfig(level=logging.INFO)
        await self.dp.start_polling(self.bot, skip_updates=True)