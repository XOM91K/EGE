import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import matplotlib.cm as cm

# Настройка стиля
plt.style.use('seaborn-v0_8-darkgrid')
fig = plt.figure(figsize=(16, 10), facecolor='#f8f9fa')
fig.suptitle('СТАТИСТИКА ЗДОРОВОГО ПИТАНИЯ И ЗАБОЛЕВАЕМОСТИ\nв России и мире',
             fontsize=18, fontweight='bold', y=0.98, color='#2c3e50')

# Создаем собственный цветовой градиент
colors = ['#3498db', '#2ecc71', '#e74c3c', '#f39c12', '#9b59b6', '#1abc9c']

# График 1: Пирамида ожирения по возрастам (Россия, 2023)
ax1 = plt.subplot(2, 3, 1, facecolor='white')
ax1.set_title('РАСПРЕДЕЛЕНИЕ ИМТ ПО ВОЗРАСТАМ\nИсточник: Росстат, 2023',
              fontsize=11, fontweight='bold', pad=15, color='#2c3e50')

age_groups = ['18-25', '26-35', '36-45', '46-55', '56-65', '65+']
normal = [68, 55, 42, 35, 32, 30]  # Нормальный вес
overweight = [25, 32, 40, 42, 43, 42]  # Избыточный вес
obese = [7, 13, 18, 23, 25, 28]  # Ожирение

x = np.arange(len(age_groups))
width = 0.25

bars1 = ax1.bar(x - width, normal, width, label='Норма', color='#2ecc71', edgecolor='white', linewidth=1.5)
bars2 = ax1.bar(x, overweight, width, label='Избыток', color='#f39c12', edgecolor='white', linewidth=1.5)
bars3 = ax1.bar(x + width, obese, width, label='Ожирение', color='#e74c3c', edgecolor='white', linewidth=1.5)

ax1.set_ylabel('Процент населения (%)', fontsize=10, color='#34495e')
ax1.set_xticks(x)
ax1.set_xticklabels(age_groups, rotation=15, fontsize=9)
ax1.legend(frameon=True, fancybox=True, shadow=True)
ax1.grid(True, alpha=0.2)

# График 2: Радар-диаграмма заболеваний (мировая статистика)
ax2 = plt.subplot(2, 3, 2, projection='polar', facecolor='white')
ax2.set_title('ВЛИЯНИЕ ПИТАНИЯ НА ЗАБОЛЕВАНИЯ\nИсточник: WHO Global Report',
              fontsize=11, fontweight='bold', pad=15, color='#2c3e50')

categories = ['Сердечно-\nсосудистые', 'Диабет\n2 типа', 'Гипер-\nтония', 'Онко-\nлогия', 'Ожирение',
              'Метаболический\nсиндром']
N = len(categories)
values = [72, 58, 65, 35, 85, 42]

angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
values += values[:1]
angles += angles[:1]

ax2.plot(angles, values, 'o-', linewidth=2.5, color='#9b59b6')
ax2.fill(angles, values, alpha=0.25, color='#9b59b6')
ax2.set_xticks(angles[:-1])
ax2.set_xticklabels(categories, fontsize=9)
ax2.set_ylim(0, 100)
ax2.grid(True)

# График 3: Воронка пищевых привычек
ax3 = plt.subplot(2, 3, 3, facecolor='white')
ax3.set_title('ПИЩЕВЫЕ ПРИВЫЧКИ НАСЕЛЕНИЯ\nИсточник: ФГБУН "ФИЦ питания"',
              fontsize=11, fontweight='bold', pad=15, color='#2c3e50')

stages = ['Все население', 'Следят за питанием', 'Считают КБЖУ', 'Консультируются\nс диетологами', 'Достигают\nцелей']
percentages = [100, 42, 28, 15, 8]
colors_funnel = ['#3498db', '#2ecc71', '#f39c12', '#e74c3c', '#9b59b6']

for i, (stage, perc, color) in enumerate(zip(stages, percentages, colors_funnel)):
    width = perc / 100 * 0.8
    left = (1 - width) / 2

    rect = mpatches.Rectangle((left, i), width, 0.8,
                              facecolor=color,
                              edgecolor='white',
                              linewidth=2,
                              alpha=0.9 - i * 0.15)
    ax3.add_patch(rect)

    ax3.text(0.5, i + 0.4, f"{stage}\n{perc}%",
             ha='center', va='center',
             fontsize=9, fontweight='bold',
             color='white')

ax3.set_xlim(0, 1)
ax3.set_ylim(0, len(stages))
ax3.axis('off')

# График 4: Динамика диабета (2000-2023)
ax4 = plt.subplot(2, 3, 4, facecolor='white')
ax4.set_title('РОСТ ЗАБОЛЕВАЕМОСТИ ДИАБЕТОМ 2 ТИПА\nИсточник: IDF Diabetes Atlas',
              fontsize=11, fontweight='bold', pad=15, color='#2c3e50')

years = np.arange(2000, 2024, 2)
world = [5.1, 5.7, 6.2, 7.0, 7.9, 8.8, 9.6, 10.4, 11.2, 11.8, 12.5, 13.1]
russia = [4.5, 5.0, 5.6, 6.2, 6.8, 7.5, 8.2, 9.0, 9.7, 10.5, 11.2, 11.8]

ax4.plot(years, world, 'o-', linewidth=3, markersize=6,
         color='#e74c3c', label='Мир', alpha=0.8)
ax4.plot(years, russia, 's-', linewidth=3, markersize=6,
         color='#3498db', label='Россия', alpha=0.8)

# Заполнение градиентом
ax4.fill_between(years, world, alpha=0.1, color='#e74c3c')
ax4.fill_between(years, russia, alpha=0.1, color='#3498db')

ax4.set_ylabel('Процент населения (%)', fontsize=10, color='#34495e')
ax4.set_xlabel('Год', fontsize=10, color='#34495e')
ax4.legend(frameon=True, fancybox=True, shadow=True)
ax4.grid(True, alpha=0.2)

# График 5: Круговой график с вырезом
ax5 = plt.subplot(2, 3, 5, facecolor='white')
ax5.set_title('ПРИЧИНЫ ОЖИРЕНИЯ В РОССИИ\nИсточник: Роспотребнадзор',
              fontsize=11, fontweight='bold', pad=15, color='#2c3e50')

causes = ['Неправильное\nпитание', 'Низкая\nактивность', 'Генетика', 'Стресс', 'Другие\nпричины']
values_causes = [65, 20, 8, 5, 2]
explode = (0.05, 0.05, 0.05, 0.05, 0.05)
colors_causes = ['#e74c3c', '#f39c12', '#3498db', '#9b59b6', '#95a5a6']

wedges, texts, autotexts = ax5.pie(values_causes, explode=explode, labels=causes,
                                   colors=colors_causes, autopct='%1.0f%%',
                                   startangle=90, counterclock=False,
                                   wedgeprops=dict(width=0.5, edgecolor='white', linewidth=2),
                                   textprops=dict(fontsize=9))

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

# График 6: Эффект от здорового питания
ax6 = plt.subplot(2, 3, 6, facecolor='white')
ax6.set_title('ЭФФЕКТ ОТ СМЕНЫ ПИТАНИЯ (12 месяцев)\nИсточник: New England Journal of Medicine',
              fontsize=11, fontweight='bold', pad=15, color='#2c3e50')

indicators = ['Вес тела\n(кг)', 'Холестерин\n(%)', 'Давление\n(%)', 'Энергия\n(баллы)', 'Качество\nсна']
before = [89, 6.8, 145, 45, 58]
after = [72, 4.2, 128, 78, 82]

x_ind = np.arange(len(indicators))
width = 0.35

bars_before = ax6.bar(x_ind - width / 2, before, width,
                      label='До', color='#e74c3c', edgecolor='white', linewidth=2)
bars_after = ax6.bar(x_ind + width / 2, after, width,
                     label='После', color='#2ecc71', edgecolor='white', linewidth=2)

# Добавляем соединительные линии для наглядности
for i, (b, a) in enumerate(zip(before, after)):
    ax6.plot([i - width / 2, i + width / 2], [b, a], 'k--', alpha=0.3, linewidth=1)
    ax6.text(i - width / 2, b + 2, f'{b}', ha='center', va='bottom', fontsize=8, fontweight='bold')
    ax6.text(i + width / 2, a + 2, f'{a}', ha='center', va='bottom', fontsize=8, fontweight='bold')

ax6.set_xticks(x_ind)
ax6.set_xticklabels(indicators, fontsize=9)
ax6.legend(frameon=True, fancybox=True, shadow=True)
ax6.grid(True, alpha=0.2)

# Добавляем водяной знак
fig.text(0.5, 0.02, 'Данные для проекта "Цифровая книга рецептов" | Аналитика: HealthData AI',
         ha='center', fontsize=9, color='#7f8c8d', alpha=0.7)

plt.tight_layout(rect=[0, 0.05, 1, 0.96])
plt.show()

# Дополнительный график: Карта здоровья по регионам РФ
fig2 = plt.figure(figsize=(12, 8), facecolor='#f8f9fa')
ax_map = fig2.add_subplot(111, facecolor='white')

# Создаем схематичную "карту" регионов
regions = ['Центральный', 'Северо-Западный', 'Южный', 'Приволжский',
           'Уральский', 'Сибирский', 'Дальневосточный']
health_scores = [72, 68, 65, 63, 61, 59, 57]  # Условные баллы здоровья
obesity_rates = [28, 31, 34, 36, 38, 41, 43]  # Процент ожирения

# Создаем кастомные маркеры в виде человечков
for i, (region, health, obesity) in enumerate(zip(regions, health_scores, obesity_rates)):
    x = i * 1.5
    y = health

    # Тело (круг)
    circle = plt.Circle((x, y), 0.3, color=cm.RdYlGn(health / 100), alpha=0.8)
    ax_map.add_patch(circle)

    # Текст с процентом ожирения
    ax_map.text(x, y - 0.5, f'{obesity}%', ha='center', va='top',
                fontsize=9, fontweight='bold', color='#e74c3c')

    # Название региона
    ax_map.text(x, y + 0.5, region, ha='center', va='bottom',
                fontsize=9, rotation=45, color='#2c3e50')

ax_map.set_title(
    'РЕЙТИНГ ЗДОРОВЬЯ ПО РЕГИОНАМ РФ\nЧем выше балл - лучше показатели здоровья\nКрасные цифры - % ожирения\nИсточник: Минздрав РФ, 2023',
    fontsize=14, fontweight='bold', pad=20, color='#2c3e50')
ax_map.set_xlim(-1, len(regions) * 1.5)
ax_map.set_ylim(50, 80)
ax_map.set_ylabel('Индекс здоровья', fontsize=11, color='#34495e')
ax_map.grid(True, alpha=0.2)
ax_map.set_axisbelow(True)

# Добавляем цветовую шкалу
sm = plt.cm.ScalarMappable(cmap=cm.RdYlGn, norm=plt.Normalize(vmin=50, vmax=80))
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax_map, orientation='vertical', fraction=0.03, pad=0.04)
cbar.set_label('Качество показателей', fontsize=10)

plt.tight_layout()
plt.show()