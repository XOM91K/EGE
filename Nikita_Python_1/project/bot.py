import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters

from config import BOT_TOKEN
from database import db
from keyboards import main_menu, recipe_navigation
from utils import format_recipe_message, get_meal_type_name

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Состояния пользователей
user_states = {}


# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    welcome_text = f"""
👋 Привет, {user.first_name}!

🍎 Добро пожаловать в Цифровую книгу рецептов здорового питания!

Выберите тип приема пищи:
• 🍳 Завтрак - легкие и питательные блюда
• 🍲 Обед - сытные и сбалансированные варианты  
• 🍽️ Ужин - легкие и полезные рецепты

Начните с выбора кнопки ниже! 👇
    """

    await update.message.reply_text(welcome_text, reply_markup=main_menu())


# Обработка текстовых сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    chat_id = update.message.chat_id

    if text == "🍳 Завтрак":
        await show_recipes(update, context, 'breakfast', 0)
    elif text == "🍲 Обед":
        await show_recipes(update, context, 'lunch', 0)
    elif text == "🍽️ Ужин":
        await show_recipes(update, context, 'dinner', 0)
    elif text == "ℹ️ О боте":
        about_text = """
📚 Цифровая книга рецептов здорового питания

Этот бот поможет вам:
• Найти полезные рецепты для любого приема пищи
• Узнать пищевую ценность блюд
• Следить за здоровым питанием

Для начала работы выберите тип приема пищи!
        """
        await update.message.reply_text(about_text, reply_markup=main_menu())
    else:
        await update.message.reply_text("Пожалуйста, используйте кнопки меню 👇", reply_markup=main_menu())


# Показать рецепт
async def show_recipes(update: Update, context: ContextTypes.DEFAULT_TYPE, meal_type: str, index: int):
    recipe = db.get_recipe(meal_type, index)

    if not recipe:
        await update.message.reply_text("Рецепты не найдены 😔")
        return

    # Формируем сообщение
    message = format_recipe_message(recipe)

    # Отправляем фото и сообщение
    try:
        with open(recipe['image'], 'rb') as photo:
            if isinstance(update, Update) and update.message:
                sent_message = await update.message.reply_photo(
                    photo=photo,
                    caption=message,
                    parse_mode='Markdown',
                    reply_markup=recipe_navigation(index, db.get_total_recipes(meal_type), meal_type)
                )
            else:
                # Для callback queries
                await update.callback_query.message.reply_photo(
                    photo=photo,
                    caption=message,
                    parse_mode='Markdown',
                    reply_markup=recipe_navigation(index, db.get_total_recipes(meal_type), meal_type)
                )
    except FileNotFoundError:
        if isinstance(update, Update) and update.message:
            await update.message.reply_text(
                message,
                parse_mode='Markdown',
                reply_markup=recipe_navigation(index, db.get_total_recipes(meal_type), meal_type)
            )
        else:
            await update.callback_query.message.reply_text(
                message,
                parse_mode='Markdown',
                reply_markup=recipe_navigation(index, db.get_total_recipes(meal_type), meal_type)
            )


# Обработка callback queries (кнопки навигации)
async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "main_menu":
        await query.message.reply_text("Выберите тип приема пищи:", reply_markup=main_menu())
    elif data.startswith("recipe_"):
        # Формат: recipe_{meal_type}_{index}
        parts = data.split("_")
        if len(parts) == 3:
            meal_type = parts[1]
            index = int(parts[2])
            await show_recipes(update, context, meal_type, index)


# Обработка ошибок
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.error(f"Ошибка: {context.error}")
    if update and update.message:
        await update.message.reply_text("Произошла ошибка. Попробуйте еще раз.")


# Основная функция
def main():
    # Создаем приложение
    application = Application.builder().token(BOT_TOKEN).build()

    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(CallbackQueryHandler(handle_callback))

    # Обработчик ошибок
    application.add_error_handler(error_handler)

    # Запускаем бота
    print("Бот запущен...")
    application.run_polling()


if __name__ == '__main__':
    main()