import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Wedge

# Настройка стиля
plt.style.use('seaborn-v0_8')
fig = plt.figure(figsize=(15, 10))

# График 1: Распространенность ожирения по возрастным группам
plt.subplot(2, 2, 1)
age_groups = ['18-25', '26-35', '36-45', '46-55', '56-65', '65+']
obesity_rates = [22, 35, 48, 52, 47, 41]
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57', '#FF9FF3']

bars = plt.bar(age_groups, obesity_rates, color=colors, alpha=0.8)
plt.title('РАСПРОСТРАНЕННОСТЬ ОЖИРЕНИЯ\nПО ВОЗРАСТНЫМ ГРУППАМ', fontsize=12, fontweight='bold', pad=20)
plt.ylabel('Процент населения (%)', fontsize=10)
plt.ylim(0, 60)

# Добавляем значения на столбцы
for bar, value in zip(bars, obesity_rates):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, f'{value}%',
             ha='center', va='bottom', fontweight='bold')

plt.grid(True, alpha=0.3)

# График 2: Статистика заболеваний, связанных с питанием
plt.subplot(2, 2, 2)
diseases = ['Сердечно-сосудистые', 'Диабет 2 типа', 'Гипертония', 'Онкология']
percentages = [68, 45, 72, 35]
colors_disease = ['#E15759', '#76B7B2', '#59A14F', '#EDC948']

wedges, texts, autotexts = plt.pie(percentages, labels=diseases, autopct='%1.0f%%',
                                   colors=colors_disease, startangle=90)
plt.title('ЗАБОЛЕВАНИЯ, СВЯЗАННЫЕ С НЕПРАВИЛЬНЫМ ПИТАНИЕМ', fontsize=12, fontweight='bold', pad=20)

# Улучшаем читаемость
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

# График 3: Приверженность здоровому питанию
plt.subplot(2, 2, 3)
categories = ['Следят за питанием', 'Периодически следят', 'Не следят', 'Не интересуются']
values = [28, 35, 22, 15]
colors_habits = ['#2E8B57', '#87CEEB', '#CD5C5C', '#A9A9A9']

plt.barh(categories, values, color=colors_habits, alpha=0.8)
plt.title('ПРИВЕРЖЕННОСТЬ ЗДОРОВОМУ ПИТАНИЮ', fontsize=12, fontweight='bold', pad=20)
plt.xlabel('Процент населения (%)', fontsize=10)

for i, v in enumerate(values):
    plt.text(v + 1, i, f'{v}%', va='center', fontweight='bold')

plt.grid(True, alpha=0.3)

# График 4: Динамика заболеваемости диабетом
plt.subplot(2, 2, 4)
years = [2015, 2017, 2019, 2021, 2023]
diabetes_rates = [7.2, 8.1, 9.3, 10.5, 11.8]

plt.plot(years, diabetes_rates, marker='o', linewidth=3, markersize=8,
         color='#DC143C', alpha=0.8)
plt.fill_between(years, diabetes_rates, alpha=0.2, color='#DC143C')
plt.title('ДИНАМИКА ЗАБОЛЕВАЕМОСТИ ДИАБЕТОМ 2 ТИПА', fontsize=12, fontweight='bold', pad=20)
plt.ylabel('Процент населения (%)', fontsize=10)
plt.xlabel('Год', fontsize=10)

# Добавляем аннотации
for i, (year, rate) in enumerate(zip(years, diabetes_rates)):
    plt.annotate(f'{rate}%', (year, rate), textcoords="offset points",
                 xytext=(0,10), ha='center', fontweight='bold')

plt.grid(True, alpha=0.3)

plt.tight_layout(pad=3.0)
plt.show()

# Дополнительный график: Экономические потери
plt.figure(figsize=(10, 6))
categories_econ = ['Медицинские расходы', 'Потери производительности', 'Инвалидность', 'Преждевременная смертность']
losses = [45, 28, 15, 12]
colors_econ = ['#FF9999', '#66B3FF', '#99FF99', '#FFD700']

plt.bar(categories_econ, losses, color=colors_econ, alpha=0.8)
plt.title('ЭКОНОМИЧЕСКИЕ ПОТЕРИ ОТ ПРОБЛЕМ ПИТАНИЯ\n(в % от общих затрат)',
          fontsize=14, fontweight='bold', pad=20)
plt.ylabel('Процент от общих потерь (%)', fontsize=11)

for i, v in enumerate(losses):
    plt.text(i, v + 1, f'{v}%', ha='center', va='bottom', fontweight='bold', fontsize=10)

plt.xticks(rotation=15)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# График сравнения: Здоровое vs Нездоровое питание
plt.figure(figsize=(12, 6))

# Данные для сравнения
metrics = ['Риск сердечных\nзаболеваний', 'Риск диабета', 'Уровень энергии', 'Качество сна', 'Продолжительность\nжизни']
healthy = [15, 12, 85, 78, 82]
unhealthy = [65, 58, 45, 52, 65]

x = np.arange(len(metrics))
width = 0.35

plt.bar(x - width/2, healthy, width, label='Здоровое питание', color='#2E8B57', alpha=0.8)
plt.bar(x + width/2, unhealthy, width, label='Нездоровое питание', color='#CD5C5C', alpha=0.8)

plt.title('СРАВНЕНИЕ ПОКАЗАТЕЛЕЙ ЗДОРОВЬЯ\nПРИ РАЗНЫХ ТИПАХ ПИТАНИЯ', fontsize=14, fontweight='bold', pad=20)
plt.ylabel('Оценка (0-100)', fontsize=11)
plt.xticks(x, metrics)
plt.legend()

# Добавляем значения на столбцы
for i, v in enumerate(healthy):
    plt.text(i - width/2, v + 2, f'{v}', ha='center', va='bottom', fontweight='bold')
for i, v in enumerate(unhealthy):
    plt.text(i + width/2, v + 2, f'{v}', ha='center', va='bottom', fontweight='bold')

plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()