from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


# Главное меню
def main_menu():
    return ReplyKeyboardMarkup([
        [KeyboardButton("🍳 Завтрак"), KeyboardButton("🍲 Обед")],
        [KeyboardButton("🍽️ Ужин"), KeyboardButton("ℹ️ О боте")]
    ], resize_keyboard=True)


# Кнопки для навигации по рецептам
def recipe_navigation(current_index, total_recipes, meal_type):
    keyboard = []

    # Кнопки вперед/назад
    nav_buttons = []
    if current_index > 0:
        nav_buttons.append(InlineKeyboardButton("⬅️ Назад", callback_data=f"recipe_{meal_type}_{current_index - 1}"))

    nav_buttons.append(InlineKeyboardButton(f"{current_index + 1}/{total_recipes}", callback_data="count"))

    if current_index < total_recipes - 1:
        nav_buttons.append(InlineKeyboardButton("Вперед ➡️", callback_data=f"recipe_{meal_type}_{current_index + 1}"))

    if nav_buttons:
        keyboard.append(nav_buttons)

    # Кнопка возврата в меню
    keyboard.append([InlineKeyboardButton("📋 В главное меню", callback_data="main_menu")])

    return InlineKeyboardMarkup(keyboard)