from dotenv import load_dotenv
import os

from telegram.ext import Application
from utils import get_logger
from handlers.commands import (
    start_handler, help_handler, brekkie_handler, dinz_handler, makan_handler, clear_handler
)
from handlers.buttons import button_handler

# Load environment variables
load_dotenv()

TOKEN = os.getenv("TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME")

# Logger setup
logger = get_logger(__name__)

# Main
if __name__ == "__main__":
    logger.info("Starting bot...")

    if not TOKEN:
        logger.error("Bot token not found! Check your .env file.")
        exit(1)

    if not BOT_USERNAME:
        logger.warning("Bot username not found! Defaulting to unknown.")

    app = Application.builder().token(TOKEN).build()

    # Command handlers
    logger.info("Registering command handlers...")
    app.add_handler(start_handler)
    logger.debug("Start handler registered.")
    app.add_handler(help_handler)
    logger.debug("Help handler registered.")
    app.add_handler(brekkie_handler)
    logger.debug("Breakfast handler registered.")
    app.add_handler(dinz_handler)
    logger.debug("Dinner handler registered.")
    app.add_handler(makan_handler)
    logger.debug("Makan handler registered.")
    app.add_handler(clear_handler)
    logger.debug("Clear handler registered.")

    # Callback query handler
    logger.debug("Registering button handler...")
    app.add_handler(button_handler)

    # Poll the bot
    try:
        logger.info("Polling started. Bot is running...")
        app.run_polling(poll_interval=3)
    except Exception as e:
        logger.exception("An error occurred while polling:")