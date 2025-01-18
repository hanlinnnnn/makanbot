from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes, CallbackQueryHandler
from models.user_data import user_selected_slots, user_meal_times
from constants.meal_times import BREAKFAST_TIMES, DINNER_TIMES
from utils import get_logger

logger = get_logger(__name__)

def generate_keyboard(options, selected, callback_prefix, row_size=4):
    """Generate a keyboard for selecting meal times."""
    keyboard = []
    for i in range(0, len(options), row_size):
        row = [
            InlineKeyboardButton(
                f"{'✅ ' if time in selected else ''}{time}",
                callback_data=f"{callback_prefix}_{time}"
            ) for time in options[i:i+row_size]
        ]
        keyboard.append(row)
    return keyboard

# Callback Handlers
async def button_commands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button interactions for selecting meal timings."""
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    username = query.from_user.first_name

    if user_id not in user_selected_slots:
        user_selected_slots[user_id] = {"breakfast": set(), "dinner": set()}

    data = query.data

    if data == "choose_breakfast":
        keyboard = generate_keyboard(BREAKFAST_TIMES, user_selected_slots[user_id]["breakfast"], "toggle_breakfast")
        keyboard.append([
            InlineKeyboardButton("Confirm", callback_data="confirm_breakfast"),
            InlineKeyboardButton("Cancel", callback_data="cancel")
        ])

        await query.edit_message_text(
            "Select your breakfast timings:", reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif data == "choose_dinner":
        keyboard = generate_keyboard(DINNER_TIMES, user_selected_slots[user_id]["dinner"], "toggle_dinner")
        keyboard.append([
            InlineKeyboardButton("Confirm", callback_data="confirm_dinner"),
            InlineKeyboardButton("Cancel", callback_data="cancel")
        ])

        await query.edit_message_text(
            "Select your dinner timings:", reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif data.startswith("toggle_breakfast_"):
        selected_time = data.replace("toggle_breakfast_", "")

        if selected_time in user_selected_slots[user_id]["breakfast"]:
            user_selected_slots[user_id]["breakfast"].remove(selected_time)
        else:
            user_selected_slots[user_id]["breakfast"].add(selected_time)

        keyboard = generate_keyboard(BREAKFAST_TIMES, user_selected_slots[user_id]["breakfast"], "toggle_breakfast")
        keyboard.append([
            InlineKeyboardButton("Confirm", callback_data="confirm_breakfast"),
            InlineKeyboardButton("Cancel", callback_data="cancel")
        ])

        await query.edit_message_text(
            "Select your breakfast timings:", reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif data.startswith("toggle_dinner_"):
        selected_time = data.replace("toggle_dinner_", "")

        if selected_time in user_selected_slots[user_id]["dinner"]:
            user_selected_slots[user_id]["dinner"].remove(selected_time)
        else:
            user_selected_slots[user_id]["dinner"].add(selected_time)

        keyboard = generate_keyboard(DINNER_TIMES, user_selected_slots[user_id]["dinner"], "toggle_dinner")
        keyboard.append([
            InlineKeyboardButton("Confirm", callback_data="confirm_dinner"),
            InlineKeyboardButton("Cancel", callback_data="cancel")
        ])

        await query.edit_message_text(
            "Select your dinner timings:", reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif data == "confirm_breakfast":
        if user_id not in user_meal_times:
            user_meal_times[user_id] = {"username": username, "breakfast_times": [], "dinner_times": []}

        user_meal_times[user_id]["breakfast_times"] = sorted(user_selected_slots[user_id]["breakfast"])
        await query.edit_message_text(
            f"Breakfast times confirmed: {', '.join(user_meal_times[user_id]['breakfast_times'])}\nCheck out when others are brekking! /brekkie"
        )
        logger.info(f"User {username} ({user_id}) confirmed breakfast times: {user_selected_slots[user_id]['breakfast']}")

    elif data == "confirm_dinner":
        if user_id not in user_meal_times:
            user_meal_times[user_id] = {"username": username, "breakfast_times": [], "dinner_times": []}

        user_meal_times[user_id]["dinner_times"] = sorted(user_selected_slots[user_id]["dinner"])
        await query.edit_message_text(
            f"Dinner times confirmed: {', '.join(user_meal_times[user_id]['dinner_times'])}\nCheck out when others are dinzing! /dinz"
        )
        logger.info(f"User {username} ({user_id}) confirmed dinner times: {user_selected_slots[user_id]['dinner']}")

    elif data == "cancel":
        user_selected_slots[user_id] = {"breakfast": set(), "dinner": set()}
        await query.edit_message_text("Selection canceled.")
        logger.info(f"User {username} ({user_id}) canceled their selection.")

button_handler = CallbackQueryHandler(button_commands)