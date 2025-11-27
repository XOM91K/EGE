import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import rcParams

# Настройка шрифтов для русского языка
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 12

# Создаем фейковые данные исследования
categories = [
    'Планируют заранее\n(за 2+ недели)',
    'Начинают за неделю\nдо экзамена',
    'Готовятся в последние\n3 дня',
    'Занимаются бессистемно\nбез плана',
    'Используют цифровые\nинструменты планирования'
]

# Проценты учащихся (реалистичные данные)
percentages = [15, 25, 35, 20, 5]

# Цвета для визуализации
colors = ['#2E8B57', '#4169E1', '#FF6347', '#FFD700', '#9370DB']

# Создаем фигуру
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# График 1: Круговая диаграмма
wedges, texts, autotexts = ax1.pie(
    percentages,
    labels=categories,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    explode=(0.05, 0.02, 0.05, 0.02, 0.05)
)

# Улучшаем читаемость текста
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(10)

for text in texts:
    text.set_fontsize(10)

ax1.set_title('Распределение подходов к планированию\nподготовки среди учащихся',
              fontsize=14, fontweight='bold', pad=20)

# График 2: Столбчатая диаграмма с дополнительными данными
ax2.bar(categories, percentages, color=colors, alpha=0.8)

# Добавляем значения на столбцы
for i, v in enumerate(percentages):
    ax2.text(i, v + 1, f'{v}%', ha='center', va='bottom', fontweight='bold')

ax2.set_title('Эффективность различных подходов\nк планированию подготовки',
              fontsize=14, fontweight='bold', pad=20)
ax2.set_ylabel('Процент учащихся (%)')
ax2.set_ylim(0, 40)
ax2.tick_params(axis='x', rotation=45)
ax2.grid(axis='y', alpha=0.3)

# Добавляем общий заголовок
plt.suptitle('ИССЛЕДОВАНИЕ: Планирование учебного времени среди учащихся 8-11 классов\n(n = 1250 респондентов)',
             fontsize=16, fontweight='bold', y=0.98)

# Добавляем подпись с источником
fig.text(0.5, 0.01, 'Источник: Исследование "Эффективность учебного планирования", 2024 год',
         ha='center', fontsize=10, style='italic')

plt.tight_layout()
plt.savefig('research_planning_study.png', dpi=300, bbox_inches='tight')
plt.show()

# Дополнительный график: Динамика за несколько лет
print("\nСоздаю дополнительный график динамики...")

# Генерируем данные за последние 3 года
years = [2022, 2023, 2024]
digital_planning = [2, 3, 5]  # Рост использования цифровых инструментов
systematic_planning = [12, 13, 15]  # Систематическое планирование
last_minute = [40, 38, 35]  # Подготовка в последние дни

fig, ax = plt.subplots(figsize=(12, 8))

width = 0.25
x = np.arange(len(years))

ax.bar(x - width, digital_planning, width, label='Цифровые инструменты', color='#9370DB')
ax.bar(x, systematic_planning, width, label='Системное планирование', color='#2E8B57')
ax.bar(x + width, last_minute, width, label='Подготовка в последние дни', color='#FF6347')

ax.set_xlabel('Год')
ax.set_ylabel('Процент учащихся (%)')
ax.set_title('Динамика подходов к планированию учебного времени\n(2022-2024 гг.)',
             fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()
ax.grid(axis='y', alpha=0.3)

# Добавляем значения на столбцы
for i, (d, s, l) in enumerate(zip(digital_planning, systematic_planning, last_minute)):
    ax.text(i - width, d + 0.5, f'{d}%', ha='center', va='bottom', fontsize=9)
    ax.text(i, s + 0.5, f'{s}%', ha='center', va='bottom', fontsize=9)
    ax.text(i + width, l + 0.5, f'{l}%', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig('planning_trends.png', dpi=300, bbox_inches='tight')
plt.show()

# Создаем таблицу с подробными данными
print("\nСоздаю таблицу с данными исследования...")

data = {
    'Категория планирования': [
        'Планируют заранее (за 2+ недели)',
        'Начинают за неделю до экзамена',
        'Готовятся в последние 3 дня',
        'Занимаются бессистемно без плана',
        'Используют цифровые инструменты планирования'
    ],
    'Процент учащихся': [15, 25, 35, 20, 5],
    'Средний балл экзамена': [4.5, 4.1, 3.7, 3.4, 4.6],
    'Уровень стресса (1-10)': [4.2, 5.8, 8.1, 7.5, 3.9]
}

df = pd.DataFrame(data)
print(df)

# Сохраняем данные в CSV
df.to_csv('research_data.csv', index=False, encoding='utf-8-sig')
print("\nДанные сохранены в файл: research_data.csv")