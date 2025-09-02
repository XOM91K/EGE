import requests
import csv
from concurrent.futures import ThreadPoolExecutor, as_completed

# Настройки
BASE_URL = "https://stimul.sch1576.ru/api/achievements/"
SESSION_COOKIE = "SESSION=2a49a3cb5ae3d8865a34a07e66d6288a%2F7d266f6f850d5b8e740a84ebbf5b18c35dc5a27bdce786b3624384370ca054cf2d33002d334208dbc3d0c786b5b312d6cfde8158fb5236f090a075bd9454a875"
HEADERS = {
    "Cookie": SESSION_COOKIE,
    "User-Agent": "Mozilla/5.0"
}

# Списки для проверки
user_ids = [
    383, 168, 198, 539, 372, 65, 331, 302, 303, 279,
    412, 659, 218, 304, 312, 277, 227, 284, 495, 427,
    432, 90, 431, 142, 476
]

achievement_ids = [
    224, 223, 222, 221, 220, 219, 218, 217, 216, 215,
    214, 213, 212, 211, 210, 209, 208, 207, 206, 205, 204
]


def get_achievement_data(user_id, achievement_id):
    """Получает данные о конкретном достижении пользователя"""
    try:
        url = f"{BASE_URL}{achievement_id}?userId={user_id}"
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            return response.json().get("data")
    except Exception as e:
        print(f"Ошибка для user_id={user_id}, achievement_id={achievement_id}: {str(e)}")
    return None


def process_user(user_id):
    """Обрабатывает одного пользователя и возвращает строку для CSV"""
    max_points = 0
    best_category = None
    best_subcategories = []

    # Проверяем все achievement_id для пользователя
    for achievement_id in achievement_ids:
        data = get_achievement_data(user_id, achievement_id)
        if not data:
            continue

        points = data.get("points", 0)
        if points > max_points:
            max_points = points
            best_category = {
                "title": data.get("title", "")[:50],
                "full_title": data.get("title", ""),
                "points": points
            }

            # Собираем подкатегории с ненулевыми баллами
            best_subcategories = []
            for condition in data.get("conditions", []):
                user_points = condition.get("userPoints", {}).get("userPoints", 0)
                if user_points > 0:
                    best_subcategories.append({
                        "condition": condition.get("condition", ""),
                        "points": user_points
                    })

    # Формируем строку результата
    if not best_category:
        return None

    result = [
        user_id,
        f'"{best_category["title"]}"',
        best_category["points"]
    ]

    # Добавляем до 2 подкатегорий
    for sub in best_subcategories[:2]:
        result.extend([
            f'"{sub["condition"]}"',
            sub["points"]
        ])

    # Дополняем пустыми значениями, если подкатегорий меньше 2
    while len(result) < 7:  # 3 основных + 2 подкатегории * 2
        result.extend(["", ""])

    return result


# Создаем CSV файл для результатов
with open("user_achievements_report.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    writer.writerow([
        "User ID", "Category Title (50 chars)", "Total Points",
        "Subcategory 1", "Points 1",
        "Subcategory 2", "Points 2"
    ])

    # Используем ThreadPoolExecutor для ускорения обработки
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(process_user, user_id): user_id for user_id in user_ids}

        for future in as_completed(futures):
            result = future.result()
            if result:
                writer.writerow(result)
                print(f"Обработан user_id: {result[0]}")

print("Готово! Результаты сохранены в user_achievements_report.csv")