import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import matplotlib.patches as mpatches

# Настройка стиля
plt.style.use('seaborn-v0_8-darkgrid')
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 10), facecolor='#f8f9fa')
fig.suptitle(
    'СТАТИСТИКА ИСПОЛЬЗОВАНИЯ БОТА "ЦИФРОВАЯ КНИГА РЕЦЕПТОВ"\nПериод: 01.12.2025 - 31.12.2025\nВсего пользователей: 24',
    fontsize=16, fontweight='bold', y=0.98, color='#2c3e50')

# Генерация дат за декабрь 2025
dates = [datetime(2025, 12, 1) + timedelta(days=i) for i in range(31)]

# Реалистичные данные использования (симулированные)
np.random.seed(42)  # Для воспроизводимости

# График 1: Активность по дням
ax1.set_title('АКТИВНОСТЬ ПОЛЬЗОВАТЕЛЕЙ ПО ДНЯМ\n(уникальные пользователи)',
              fontsize=12, fontweight='bold', pad=15, color='#2c3e50')

# Имитация пиков в выходные и снижения в будни
daily_active = []
for i, date in enumerate(dates):
    base = 8 if date.weekday() >= 5 else 5  # Больше в выходные
    variation = np.random.randint(-2, 3)
    daily_active.append(max(1, base + variation))

ax1.bar(dates, daily_active, color='#3498db', edgecolor='white', linewidth=1.5, alpha=0.8)
ax1.axhline(y=np.mean(daily_active), color='#e74c3c', linestyle='--', linewidth=2, alpha=0.7,
            label=f'Среднее: {np.mean(daily_active):.1f}')

ax1.set_ylabel('Количество активных пользователей', fontsize=10, color='#34495e')
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m'))
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=5))
ax1.legend(frameon=True, fancybox=True, shadow=True)
ax1.grid(True, alpha=0.2)
ax1.set_ylim(0, 12)

# График 2: Распределение по времени суток
ax2.set_title('АКТИВНОСТЬ ПО ВРЕМЕНАМ СУТОК\n(всего взаимодействий)',
              fontsize=12, fontweight='bold', pad=15, color='#2c3e50')

hours = list(range(24))
# Пики: утро (7-9), обед (12-14), вечер (18-21)
hourly_activity = [2, 1, 0, 0, 1, 3, 8, 12, 10, 7, 5, 9, 11, 10, 6, 5, 4, 7, 14, 11, 8, 5, 3, 2]

ax2.bar(hours, hourly_activity, color='#2ecc71', edgecolor='white', linewidth=1.5, alpha=0.8)

# Выделяем пиковые часы
peak_hours = [7, 8, 12, 13, 18, 19]
for hour in peak_hours:
    ax2.bar(hour, hourly_activity[hour], color='#e74c3c', edgecolor='white', linewidth=1.5, alpha=0.9)

ax2.set_xlabel('Час суток', fontsize=10, color='#34495e')
ax2.set_ylabel('Количество взаимодействий', fontsize=10, color='#34495e')
ax2.set_xticks([0, 6, 12, 18, 23])
ax2.set_xticklabels(['00:00', '06:00', '12:00', '18:00', '23:00'])
ax2.grid(True, alpha=0.2)
ax2.set_ylim(0, 16)

# Добавляем аннотации для пиковых часов
ax2.text(7.5, 13, 'Утренний\nпик', ha='center', fontsize=9, fontweight='bold', color='#e74c3c')
ax2.text(12.5, 12, 'Обеденный\nпик', ha='center', fontsize=9, fontweight='bold', color='#e74c3c')
ax2.text(18.5, 15, 'Вечерний\nпик', ha='center', fontsize=9, fontweight='bold', color='#e74c3c')

# График 3: Популярность категорий рецептов
ax3.set_title('РАСПРЕДЕЛЕНИЕ ПО КАТЕГОРИЯМ РЕЦЕПТОВ\n(процент от всех просмотров)',
              fontsize=12, fontweight='bold', pad=15, color='#2c3e50')

categories = ['Завтрак', 'Обед', 'Ужин', 'Инфо о боте']
percentages = [45, 32, 18, 5]
colors_cat = ['#f39c12', '#e74c3c', '#3498db', '#95a5a6']

wedges, texts, autotexts = ax3.pie(percentages, labels=categories, colors=colors_cat,
                                   autopct='%1.0f%%', startangle=90, counterclock=False,
                                   wedgeprops=dict(edgecolor='white', linewidth=2, width=0.5),
                                   textprops=dict(fontsize=10))

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

# Выделяем самый популярный
wedges[0].set_width(0.6)

# График 4: Детализация пользователей
ax4.set_title('ДЕТАЛИЗАЦИЯ ПОЛЬЗОВАТЕЛЕЙ\n(из 24 уникальных пользователей)',
              fontsize=12, fontweight='bold', pad=15, color='#2c3e50')

user_types = ['Новые\nпользователи', 'Активные\n(>3 визита)', 'Регулярные\n(>10 визитов)', 'Вернувшиеся\nпосле паузы']
user_counts = [14, 6, 3, 1]
colors_users = ['#9b59b6', '#1abc9c', '#e67e22', '#34495e']

x_pos = np.arange(len(user_types))
bars = ax4.bar(x_pos, user_counts, color=colors_users, edgecolor='white', linewidth=2, alpha=0.9)

ax4.set_ylabel('Количество пользователей', fontsize=10, color='#34495e')
ax4.set_xticks(x_pos)
ax4.set_xticklabels(user_types, fontsize=10)
ax4.set_ylim(0, 16)

# Добавляем значения на столбцы
for bar, count in zip(bars, user_counts):
    height = bar.get_height()
    ax4.text(bar.get_x() + bar.get_width() / 2, height + 0.3, str(count),
             ha='center', va='bottom', fontweight='bold', fontsize=11)

# Добавляем процентные соотношения
total_users = sum(user_counts)
percentages_users = [count / total_users * 100 for count in user_counts]

for i, (bar, perc) in enumerate(zip(bars, percentages_users)):
    ax4.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2, f'{perc:.1f}%',
             ha='center', va='center', color='white', fontweight='bold', fontsize=10)

ax4.grid(True, alpha=0.2, axis='y')

# Добавляем общую статистику внизу
stats_text = f"""
ОБЩАЯ СТАТИСТИКА ЗА ДЕКАБРЬ 2025:
• Всего уникальных пользователей: 24
• Всего взаимодействий с ботом: 487
• Среднее время сессии: 4.2 мин
• Конверсия в активных пользователей: 37.5%
• Самый популярный рецепт: "Овсянка с ягодами" (38 просмотров)
"""
fig.text(0.5, 0.02, stats_text, ha='center', fontsize=10, color='#2c3e50',
         bbox=dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='#3498db'))

plt.tight_layout(rect=[0, 0.08, 1, 0.96])
plt.show()

# Дополнительный график: Путь пользователя
fig2 = plt.figure(figsize=(14, 8), facecolor='#f8f9fa')
ax_flow = fig2.add_subplot(111, facecolor='white')

ax_flow.set_title('ТИПИЧНЫЙ ПУТЬ ПОЛЬЗОВАТЕЛЯ В БОТЕ\n(на основе анализа 487 сессий)',
                  fontsize=14, fontweight='bold', pad=20, color='#2c3e50')

# Создаем схему воронки
steps = ['Заход в бота\n/start', 'Выбор категории\nрецепта', 'Просмотр рецепта\nс фото',
         'Навигация по\nдругим рецептам', 'Возврат в меню\nдля новой категории',
         'Повторное\nиспользование\nна след. день']
retention = [100, 82, 65, 41, 28, 15]  # Процент пользователей на каждом шаге

y_pos = np.arange(len(steps)) * 1.5

# Рисуем воронку
for i, (step, ret, y) in enumerate(zip(steps, retention, y_pos)):
    width = ret / 100 * 0.6
    left = (1 - width) / 2

    # Градиент цвета от синего к зеленому
    color = plt.cm.Blues(0.3 + i * 0.12)

    rect = mpatches.Rectangle((left, y), width, 0.8,
                              facecolor=color,
                              edgecolor='white',
                              linewidth=2.5,
                              alpha=0.9)
    ax_flow.add_patch(rect)

    # Текст внутри
    ax_flow.text(0.5, y + 0.4, f"{step}\n{ret}% пользователей",
                 ha='center', va='center',
                 fontsize=10, fontweight='bold',
                 color='white')

    # Стрелки между шагами (кроме последнего)
    if i < len(steps) - 1:
        arrow_y = y + 0.8 + 0.1
        next_y = y_pos[i + 1] - 0.1
        ax_flow.annotate('', xy=(0.5, next_y), xytext=(0.5, arrow_y),
                         arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2, alpha=0.7))

ax_flow.set_xlim(0, 1)
ax_flow.set_ylim(-0.5, len(steps) * 1.5)
ax_flow.axis('off')

# Добавляем метрики эффективности
metrics_text = f"""
МЕТРИКИ ЭФФЕКТИВНОСТИ:
• Retention Rate (1 день): 15%
• Среднее количество рецептов за сессию: 3.2
• Средняя глубина просмотра: 4.7 экранов
• Коэффициент возврата: 2.4 посещения/пользователь
"""
fig2.text(0.02, 0.02, metrics_text, fontsize=10, color='#2c3e50',
          bbox=dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='#2ecc71'))

plt.tight_layout()
plt.show()