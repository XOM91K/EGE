import numpy as np
import matplotlib.pyplot as plt

# 1. Создаем данные для графика
x = np.linspace(0, 6, 100)  # Диапазон от 0 до 6
y = (x - 3) ** 2  # Функция f(x) = (x-3)^2

# 2. Точки, в которых будем рисовать градиенты
points = [0, 2, 5]
colors = ['red', 'green', 'blue']

# 3. Создаем график
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x) = (x-3)²', linewidth=2)

# 4. Рисуем касательные (градиенты)
for point, color in zip(points, colors):
    # Значение функции в точке
    y_point = (point - 3) ** 2

    # Градиент (производная) в точке: f'(x) = 2(x-3)
    gradient = 2 * (point - 3)

    # Уравнение касательной: y = gradient * (x - point) + y_point
    tangent_line = gradient * (x - point) + y_point

    # Рисуем точку и касательную
    plt.scatter(point, y_point, color=color, s=100, zorder=5)
    plt.plot(x, tangent_line, '--', color=color,
             label=f'Градиент в x={point}: {gradient:.1f}')

    # Подписываем направление градиента
    direction = "→ минимум" if gradient < 0 else "← минимум"
    plt.text(point, y_point + 5, direction, ha='center', fontsize=10)

# 5. Настраиваем отображение
plt.axvline(3, color='black', linestyle=':', alpha=0.5, label='Минимум (x=3)')
plt.title('Градиенты функции f(x) = (x-3)²', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.grid(alpha=0.3)
plt.legend()
plt.show()