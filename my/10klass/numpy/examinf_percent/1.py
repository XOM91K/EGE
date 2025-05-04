import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def fetch_task_ids(task_type: int):
    """Получает список ID заданий для указанного типа (например, 17)."""
    url = f"https://examinf.ru/api/tasks/ids/ege/{task_type}/"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["result"]


def fetch_task_stats(task_id: int):
    """Получает статистику для конкретного задания по его ID."""
    url = f"https://examinf.ru/api/task/{task_id}/additionalInfo/"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["result"]


def calculate_percentage(correct: int, wrong: int):
    """Вычисляет процент верных решений."""
    total = correct + wrong
    return (correct / total) * 100 if total > 0 else 0.0


def analyze_task_type(task_type: int):
    """Анализирует все задания указанного типа."""
    task_ids = fetch_task_ids(task_type)
    stats = []

    for task_id in task_ids:
        try:
            data = fetch_task_stats(task_id)
            correct = data["usersSolvedCorrect"]
            wrong = data["usersSolvedWrong"]
            percentage = calculate_percentage(correct, wrong)
            stats.append({"task_id": task_id, "percentage": percentage})
        except Exception as e:
            print(f"Ошибка для задания {task_id}: {e}")

    return pd.DataFrame(stats)


# Пример для задания типа 17
task_type = 1
df = analyze_task_type(task_type)

# Сортировка по сложности (от самых сложных)
#df = df.sort_values("percentage")

# Сохранение в CSV
df.to_csv(f"ege_task_{task_type}_stats.csv", index=False)

# Визуализация
plt.figure(figsize=(12, 6))
plt.bar(df["task_id"].astype(str), df["percentage"], color="skyblue")
plt.xlabel("ID задания")
plt.ylabel("% верных решений")
plt.title(f"Сложность заданий ЕГЭ (тип {task_type})")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

# Средний процент по типу задания
mean_percentage = df["percentage"].mean()
print(f"Средний процент верных решений для заданий типа {task_type}: {mean_percentage:.2f}%")