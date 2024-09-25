import matplotlib.pyplot as plt

# Чтение данных из файла
l = [[float(d) for d in x.split()] for x in open('5.txt')]
data = l

# Инициализация параметров
k = 2
centers = [data[0], data[1]]  # Начальные центры (первые две точки)

def assign_clusters(data, centers):
    labels = []
    for point in data:
        distances = [((point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2) ** 0.5 for center in centers]
        labels.append(distances.index(min(distances)))  # Назначаем кластер
    return labels

def update_centers(data, labels, k):
    new_centers = []
    for i in range(k):
        cluster_points = [data[j] for j in range(len(data)) if labels[j] == i]
        if cluster_points:  # Проверяем, что кластер не пустой
            new_center = [sum(p[0] for p in cluster_points) / len(cluster_points),
                          sum(p[1] for p in cluster_points) / len(cluster_points)]
            new_centers.append(new_center)
        else:
            new_centers.append(centers[i])  # Если кластер пустой, оставляем старый центр
    return new_centers

# Основной цикл
plt.figure(figsize=(10, 6))  # Размер графика
for _ in range(100):  # Максимальное количество итераций
    labels = assign_clusters(data, centers)

    # Визуализация текущих точек и центров
    plt.scatter(*zip(*data), c=labels, cmap='viridis', marker='o', label='Точки')
    plt.scatter(*zip(*centers), c='red', marker='x', s=200, label='Центры')
    plt.title('Итерация')
    plt.xlabel('X координаты')
    plt.ylabel('Y координаты')
    plt.legend()
    plt.pause(0.5)  # Пауза для визуализации

    new_centers = update_centers(data, labels, k)

    if new_centers == centers:
        break  # Если центры не изменились, выходим из цикла

    centers = new_centers

# Вывод результатов
print("Центры кластеров:")
for center in centers:
    print(center)

print("\nНазначенные кластеры для точек:")
for i, label in enumerate(labels):
    print(f"Точка {data[i]} принадлежит кластеру {label}")

# Поиск точки с минимальным расстоянием до остальных точек в каждом кластере
dd = []
for i in range(k):
    cluster_points = [data[j] for j in range(len(data)) if labels[j] == i]

    if len(cluster_points) < 1:
        print(f"В кластере {i} недостаточно точек.")
        continue

    # Сумма расстояний от каждой точки до всех остальных в кластере
    distances_sum = []
    for point in cluster_points:
        total_distance = sum(
            ((point[0] - other[0]) ** 2 + (point[1] - other[1]) ** 2) ** 0.5 for other in cluster_points if
            other != point)
        distances_sum.append((total_distance, point))  # (сумма расстояний, точка)

    # Находим точку с минимальной суммой расстояний
    best_point = min(distances_sum, key=lambda x: x[0])

    print(f"\nЛучшая точка в кластере {i}:")
    print(f"Точка {best_point[1]} с суммой расстояний {best_point[0]:.2f}")
    dd.append(best_point[1])

print((dd[0][0] + dd[1][0]) / 2 * 10000)
print((dd[0][1] + dd[1][1]) / 2 * 10000)

plt.show()  # Показываем финальный график
