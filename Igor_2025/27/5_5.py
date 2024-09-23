# Чтение данных из файла
l = [[float(d) for d in x.split()] for x in open('4.txt')]
data = l

# Инициализация параметров
k = 3
centers = [data[0], data[1], data[2]]  # Начальные центры (первые две точки)
def assign_clusters(data, centers):
    labels = []
    for point in data:
        distances = [((point[0] - center[0]) **  2 + (point[1] - center[1])** 2) ** 0.5 for center in centers]
        labels.append(distances.index(min(distances)))  # Назначаем кластер
    return labels

dd = []
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
for _ in range(100):  # Максимальное количество итераций
    labels = assign_clusters(data, centers)
    new_centers = update_centers(data, labels, k)
    print(new_centers)
    if new_centers == centers:
        break  # Если центры не изменились, выходим из цикла

    centers = new_centers

# Поиск точки с минимальным расстоянием до остальных точек в каждом кластере
for i in range(k):
    cluster_points = [data[j] for j in range(len(data)) if labels[j] == i]
    # Сумма расстояний от каждой точки до всех остальных в кластере
    distances_sum = []
    for point in cluster_points:
        total_distance = sum(
            ((point[0] - other[0]) **  2 + (point[1] - other[1]) **  2) ** 0.5 for other in cluster_points if
            other != point)
        distances_sum.append((total_distance, point))  # (сумма расстояний, точка)
    # Находим точку с минимальной суммой расстояний
    best_point = min(distances_sum, key=lambda x: x[0])
    dd.append(best_point[1])
print((dd[0][0] + dd[1][0] + dd[2][0]) / 3 * 10000)
print((dd[0][1] + dd[1][1] + dd[2][1]) / 3 * 10000)