import logging
from aiogram import Bot, Dispatcher, executor, types

# --- CONFIGURATION ---
# Replace 'YOUR_BOT_TOKEN_HERE' with the token you get from BotFather
API_TOKEN = 'YOUR_BOT_TOKEN_HERE' 

# Configure logging so you can see what's happening
logging.basicConfig(level=logging.INFO)

# --- BOT INITIALIZATION ---
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# --- HANDLERS ---

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    (or presses the START button)
    """
    
    # Get user's first name to make the message personal
    user_name = message.from_user.first_name
    
    # Craft the welcome message
    hello_message = f"👋 Hello, {user_name}!"
    description = (
        "I am a simple bot created to demonstrate aiogram.\n\n"
        "Right now, I just say hello when you start!"
    )
    
    # Combine the messages
    full_message = f"{hello_message}\n\n{description}"
    
    # Send the message back to the user
    # Removed parse_mode since this message doesn't use HTML
    await message.answer(full_message)
