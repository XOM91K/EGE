import matplotlib.pyplot as plt
import numpy as np
#
# # Генерация данных
# # Гистограмма распределения
# data = np.random.gamma(2, 1.5, 1000)
# plt.hist(data, bins=30, edgecolor='black', density=True)
# plt.title('Анализ распределения (Gamma)')
# # x = np.linspace(0, 10, 100)
# # y = np.sin(x) + np.random.normal(0, 0.1, 100)
# #
# # # Scatter plot с трендом
# # plt.scatter(x, y, alpha=0.5, label='Данные')
# # plt.plot(x, np.sin(x), color='red', linewidth=2, label='Тренд')
# # plt.title('Выявление тренда в зашумленных данных')
# # plt.legend()
# plt.show()
#
# import pandas as pd
# # Загрузка CSV-файла
# df = pd.read_csv('data.csv')
# # Просмотр первых 5 строк
# print(df.head())
#
# # Удаление строк с пропусками
# df_clean = df.dropna()
# # Замена пропусков средним значением
# (df['column_name'].fillna
#  (df['column_name'].mean(), inplace=True))


# import matplotlib.pyplot as plt
# # Данные: 1000 случайных чисел с нормальным распределением
# data = np.random.normal(0, 1, 100)
# print(data)
# # Построение гистограммы
# plt.hist(data, bins=30, edgecolor='black')
# plt.title('Распределение данных')
# plt.xlabel('Значения')
# plt.ylabel('Частота')
# plt.show()

# # Данные: 3 группы с разными распределениями
# data1 = np.random.normal(0, 1, 100)
# data2 = np.random.normal(5, 2, 100)
# data3 = np.random.normal(-3, 1.5, 100)
#
# # Построение boxplot
# plt.boxplot([data1, data2, data3], labels=['Группа 1', 'Группа 2', 'Группа 3'])
# plt.title('Сравнение распределений')
# plt.ylabel('Значения')
# plt.show()

# # Данные: X и Y с линейной зависимостью + шум
# x = np.linspace(0, 10, 100)  # 100 точек от 0 до 10
# y = 2 * x + np.random.normal(0, 1, 100)  # y = 2x + шум
#
# # Построение scatter plot
# plt.scatter(x, y, alpha=0.5)
# plt.title('Зависимость Y от X')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.grid(True)
# plt.show()

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Создаем тестовый DataFrame с разными типами данных
np.random.seed(42)  # Для воспроизводимости результатов
df = pd.DataFrame({
    'Возраст': np.random.randint(18, 65, 100),
    'Зарплата': np.random.randint(30000, 150000, 100),
    'Опыт работы': np.random.randint(0, 40, 100),
    'Кредитный рейтинг': np.random.normal(500, 100, 100).astype(int),
    'Траты в месяц': np.random.randint(10000, 50000, 100)
})

# Добавляем коррелируемые колонки для демонстрации
df['Сбережения'] = df['Зарплата'] * 0.3 + np.random.normal(0, 5000, 100)
df['Ипотека'] = df['Зарплата'] * 0.4 + np.random.normal(0, 10000, 100)

# Расчет корреляционной матрицы (только для числовых колонок)
corr = df.corr()

# Визуализация heatmap с настройками
plt.figure(figsize=(10, 8))  # Размер графика
sns.heatmap(
    corr,                     # Матрица корреляций
    annot=True,               # Показывать значения в ячейках
    cmap='coolwarm',          # Цветовая схема (синий-белый-красный)
    vmin=-1, vmax=1,          # Диапазон значений корреляции
    linewidths=0.5,           # Ширина линий между ячейками
    annot_kws={'size': 10}    # Размер шрифта для аннотаций
)

# Настройки отображения
plt.title('Матрица корреляций между параметрами', pad=20, fontsize=15)
plt.xticks(rotation=45, ha='right')  # Наклон подписей оси X
plt.tight_layout()  # Автоматическая подгонка элементов
plt.show()
