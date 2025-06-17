import math
from collections import Counter


def load_data(filename):
    """Загружает данные из файла в формате: x y class_label"""
    points = []
    labels = []
    pnts = [[float(d.replace(',','.')) for d in x.split()] for x in open(filename).readlines()]
    for point in pnts:
        points.append((point[0], point[1]))
        labels.append(int(point[2]))
    return points, labels


def knn_predict(train_points, train_labels, new_point, k=3):
    # 1. Считаем расстояния от новой точки до всех остальных
    distances = []
    for i, (x, y) in enumerate(train_points):
        dist = math.dist(new_point, (x, y))  # Евклидово расстояние
        distances.append((dist, train_labels[i]))

    # 2. Сортируем точки по расстоянию и берем k ближайших
    distances.sort()  # Сортировка по первому элементу (distance)
    k_nearest_labels = [label for (dist, label) in distances[:k]]

    # 3. Выбираем самый частый класс среди соседей
    most_common = Counter(k_nearest_labels).most_common(1)
    return most_common[0][0]


# Пример использования
points, labels = [x for x in load_data('points.txt')]
print(points)
print(labels)

new_point = (3.5115221,	7.3621211)
predicted_class = knn_predict(points, labels, new_point, k=7)
print(f"Точка {new_point} относится к классу: {predicted_class}")