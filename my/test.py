import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Исходный список чисел
l = [2, 3, 4, 1, 1, 5, 6]

# Создание префиксной суммы
pr_l = [0]
for i in range(len(l)):
    pr_l.append(pr_l[-1] + l[i])

# Функция для обновления графика
def update(frame):
    plt.cla()
    plt.bar(range(len(l) + 1), pr_l[:frame+1], color='skyblue')
    plt.xticks(range(len(l) + 1), range(len(l) + 1))  # Установка делений без меток
    plt.title('Построение префиксной суммы')
    plt.xlabel('Индекс')
    plt.ylabel('Префиксная сумма')

# Создание анимации
fig = plt.figure()
animation = FuncAnimation(fig, update, frames=len(l)+1, repeat=False)

plt.show()
