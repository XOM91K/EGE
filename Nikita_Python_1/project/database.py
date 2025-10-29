import json
import os


class RecipeDatabase:
    def __init__(self, file_path='recipes.json'):
        self.file_path = file_path
        self.load_data()

    def load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
        else:
            raise FileNotFoundError(f"Файл {self.file_path} не найден")

    def get_meal_types(self):
        return list(self.data.keys())

    def get_recipes_by_meal(self, meal_type):
        return self.data.get(meal_type, [])

    def get_recipe(self, meal_type, index):
        recipes = self.get_recipes_by_meal(meal_type)
        if 0 <= index < len(recipes):
            return recipes[index]
        return None

    def get_total_recipes(self, meal_type):
        return len(self.get_recipes_by_meal(meal_type))


# Глобальный экземпляр базы данных
db = RecipeDatabase()