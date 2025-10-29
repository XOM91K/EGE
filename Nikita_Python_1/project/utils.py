def format_recipe_message(recipe):
    """Форматирует сообщение с рецептом"""
    if not recipe:
        return "Рецепт не найден"

    message = f"🍽️ *{recipe['name']}*\n\n"
    message += f"📋 *Рецепт:*\n{recipe['recipe']}\n\n"
    message += f"📊 *Пищевая ценность:*\n"
    message += f"• Калории: {recipe['calories']} ккал\n"
    message += f"• Белки: {recipe['protein']}г\n"
    message += f"• Углеводы: {recipe['carbs']}г\n"
    message += f"• Жиры: {recipe['fat']}г"

    return message


def get_meal_type_name(meal_type):
    """Возвращает русское название типа приема пищи"""
    names = {
        'breakfast': 'Завтрак',
        'lunch': 'Обед',
        'dinner': 'Ужин'
    }
    return names.get(meal_type, meal_type)