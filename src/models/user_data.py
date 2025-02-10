from collections import defaultdict

user_selected_slots = {}
user_meal_times = {}

def init_user_data(user_id):
    """Initialize user data if not already present."""
    if user_id not in user_selected_slots:
        user_selected_slots[user_id] = {"breakfast": set(), "dinner": set()}
    if user_id not in user_meal_times:
        user_meal_times[user_id] = {"username": "", "breakfast_times": [], "dinner_times": []}