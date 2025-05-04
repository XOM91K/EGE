import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from typing import List, Dict

# Настройки для красивого отображения графиков
plt.style.use('seaborn')
plt.rcParams['font.size'] = 12


def fetch_task_ids(task_type: int) -> List[int]:
    """Получает список ID заданий для указанного типа (например, 17)."""
    url = f"https://examinf.ru/api/tasks/ids/ege/{task_type}/"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["result"]


def fetch_task_stats(task_id: int) -> Dict:
    """Получает статистику для конкретного задания по его ID."""
    url = f"https://examinf.ru/api/task/{task_id}/additionalInfo/"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["result"]


def calculate_percentage(correct: int, wrong: int) -> float:
    """Вычисляет процент верных решений."""
    total = correct + wrong
    return (correct / total) * 100 if total > 0 else 0.0


def analyze_task_type(task_type: int) -> float:
    """Анализирует все задания указанного типа и возвращает средний процент."""
    task_ids = fetch_task_ids(task_type)
    percentages = []

    for task_id in task_ids:
        try:
            data = fetch_task_stats(task_id)
            correct = data["usersSolvedCorrect"]
            wrong = data["usersSolvedWrong"]
            percentage = calculate_percentage(correct, wrong)
            percentages.append(percentage)
        except Exception as e:
            print(f"Ошибка для задания {task_id} (тип {task_type}): {e}")

    return np.mean(percentages) if percentages else 0.0


# Список всех типов заданий (1-19, 22-27)
task_types = list(range(1, 20)) + list(range(22, 28))

# Собираем средние проценты для каждого типа
results = []
for task_type in task_types:
    mean_percentage = analyze_task_type(task_type)
    results.append({"Тип задания": task_type, "Средний процент": mean_percentage})
    print(f"Тип {task_type}: {mean_percentage:.2f}%")

# Создаем DataFrame и сортируем по сложности (от самых сложных)
df = pd.DataFrame(results)
df = df.sort_values("Средний процент")

# Сохраняем в CSV
df.to_csv("ege_task_difficulty.csv", index=False)

# Визуализация
plt.figure(figsize=(14, 7))
bars = plt.bar(
    df["Тип задания"].astype(str),
    df["Средний процент"],
    color=plt.cm.plasma(df["Средний процент"] / 100)  # Градиент по сложности
)

# Добавляем подписи значений
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height - 5,
        f"{height:.1f}%",
        ha="center",
        color="white" if height < 50 else "black"
    )

plt.xlabel("Тип задания ЕГЭ")
plt.ylabel("Средний % верных решений")
plt.title("Сложность заданий ЕГЭ по информатике (чем ниже %, тем сложнее)")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.ylim(0, 100)
plt.tight_layout()
plt.show()