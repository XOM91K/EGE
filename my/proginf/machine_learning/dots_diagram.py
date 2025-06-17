import matplotlib.pyplot as plt

# Данные: x, y, класс
data = [
    [3.9638064, 7.1285385, 1],
    [4.1852033, 6.1452368, 2],
    [3.8438473, 7.1735053, 1],
    [3.1628167, 6.4672343, 1],
    [3.9439358, 6.3825478, 1],
    [3.6610863, 5.9799141, 1],
    [3.9194596, 7.6652859, 1],
    [4.492111, 6.6355507, 2],
    [4.0589284, 8.3790031, 1],
    [3.9301169, 7.0770144, 2],
    [3.7768029, 6.3266337, 1],
    [4.1557779, 7.6264934, 2],
    [4.26467, 7.341128, 2],
    [3.4187624, 5.6849628, 1],
    [3.437917, 6.0425659, 1],
    [4.146096, 6.997676, 1],
    [3.6585214, 6.0361505, 1],
    [3.6345589, 8.5976575, 1],
    [3.7942096, 6.6135634, 2],
    [4.4663303, 5.082353, 2],
    [3.4204597, 5.7287691, 2],
    [3.8136644, 8.0814763, 2],
    [3.1465055, 5.4875173, 1],
    [3.7553337, 7.0652113, 3]
]

# Разделяем данные по классам
class1 = [point for point in data if point[2] == 1]
class2 = [point for point in data if point[2] == 2]
class3 = [point for point in data if point[2] == 3]

# Создаем график
plt.figure(figsize=(10, 6))

# Рисуем точки каждого класса с разными цветами
plt.scatter(
    [point[0] for point in class1],
    [point[1] for point in class1],
    color='blue',
    label='Class 1',
    s = 200
)

plt.scatter(
    [point[0] for point in class2],
    [point[1] for point in class2],
    color='green',
    label='Class 2',
    s = 200
)

plt.scatter(
    [point[0] for point in class3],
    [point[1] for point in class3],
    color='red',
    label='Class 3',
    s=300  # Делаем точку 3-го класса больше
)

# Настройки графика
plt.title('Точечная диаграмма классов')
plt.xlabel('X координата')
plt.ylabel('Y координата')
plt.grid(True, linestyle='--', alpha=0.9)
plt.legend()

# Показываем график
plt.show()