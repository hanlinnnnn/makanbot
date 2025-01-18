from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler
from collections import defaultdict
from models.user_data import user_selected_slots, user_meal_times

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start command to greet the user."""
    await update.message.reply_text(
        "Hello! I’m your MakanPlsAkuHungsBot. Use /help to see what I can do!"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Help command to display available bot commands."""
    help_text = (
        "Here are my commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/brekkie - See everyone's breakfast timings\n"
        "/dinz - See everyone's dinner timings\n"
        "/makan - Choose your breakfast or dinner timings\n"
        "/clear - Clear all your breakfast and dinner timings"
    )
    await update.message.reply_text(help_text)

async def brekkie_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Command to display everyone's breakfast times."""
    if not user_meal_times:
        await update.message.reply_text("No breakfast times set yet.")
        return

    # Organize breakfast times
    time_slots = defaultdict(list)
    total_users = 0

    for user, data in user_meal_times.items():
        if "breakfast_times" in data and data["breakfast_times"]:
            total_users += 1
            for time in data["breakfast_times"]:
                time_slots[time].append(data["username"])

    if total_users == 0:
        await update.message.reply_text("No breakfast times set yet.")
        return

    # Generate response
    response = "Breakfast Times:\n"
    for time, users in sorted(time_slots.items()):
        percentage = (len(users) / total_users) * 100
        response += f"{time} - {', '.join(users)} ({percentage:.0f}%)\n"

    await update.message.reply_text(response)

async def dinz_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Command to display everyone's dinner times."""
    if not user_meal_times:
        await update.message.reply_text("No dinner times set yet.")
        return

    # Organize dinner times
    time_slots = defaultdict(list)
    total_users = 0

    for user, data in user_meal_times.items():
        if "dinner_times" in data and data["dinner_times"]:
            total_users += 1
            for time in data["dinner_times"]:
                time_slots[time].append(data["username"])

    if total_users == 0:
        await update.message.reply_text("No dinner times set yet.")
        return

    # Generate response
    response = "Dinner Times:\n"
    for time, users in sorted(time_slots.items()):
        percentage = (len(users) / total_users) * 100
        response += f"{time} - {', '.join(users)} ({percentage:.0f}%)\n"

    await update.message.reply_text(response)

async def makan_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Command to allow users to choose between breakfast and dinner, then select timings."""
    keyboard = [
        [InlineKeyboardButton("Breakfast", callback_data="choose_breakfast")],
        [InlineKeyboardButton("Dinner", callback_data="choose_dinner")],
    ]

    await update.message.reply_text(
        "Choose your meal time type (Breakfast or Dinner):", reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def clear_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Clear all the user's breakfast and dinner timings."""
    user_id = update.effective_user.id

    user_selected_slots.pop(user_id, None)
    user_meal_times.pop(user_id, None)

    await update.message.reply_text("All your breakfast and dinner timings have been cleared!")
    

start_handler = CommandHandler("start", start_command)
help_handler = CommandHandler("help", help_command)
brekkie_handler = CommandHandler("brekkie", brekkie_command)
dinz_handler = CommandHandler("dinz", dinz_command)
makan_handler = CommandHandler("makan", makan_command)
clear_handler = CommandHandler("clear", clear_command)