import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# --- BOT INITIALIZATION ---
# Get bot token from environment
bot_token = os.getenv("BOT_TOKEN")

if not bot_token:
    logger.error("BOT_TOKEN not found in environment variables!")
    raise SystemExit("BOT_TOKEN not found in environment variables!")

# Initialize bot and dispatcher
bot = Bot(token=bot_token)
dp = Dispatcher()

logger.info("Bot initialized successfully")


# --- HANDLERS ---

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message) -> None:
    """Handle /start and /help commands with a personalized greeting."""
    user_name = message.from_user.first_name or "User"
    
    welcome_text = (
        f"👋 Hello, {user_name}!\n\n"
        "I am a simple bot created to demonstrate aiogram.\n\n"
        "Right now, I just say hello when you start!"
    )
    
    await message.answer(welcome_text)
    logger.info(f"Welcome message sent to user {message.from_user.id}")

async def _main() -> None:
    """Start the bot polling loop with graceful shutdown."""
    logger.info("Starting bot polling...")
    try:
        await dp.start_polling(bot, skip_updates=True)
    except KeyboardInterrupt:
        logger.info("Polling interrupted by user")
    finally:
        logger.info("Closing bot session...")
        await bot.session.close()
        logger.info("Bot session closed")


if __name__ == "__main__":
    logger.info("Bot application started")
    asyncio.run(_main())