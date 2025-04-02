import random
import math


def read_points(filename):
    points = []
    with open(filename, 'r') as f:
        for line in f:
            x, y = line.strip().replace(',', '.').split()
            points.append([float(x), float(y)])
    return points


def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def remove_outliers(points, K):
    outliers_removed = []
    for i, point in enumerate(points):
        is_outlier = True
        for j, other_point in enumerate(points):
            if i != j and euclidean_distance(point, other_point) <= K:
                is_outlier = False
                break
        if not is_outlier:
            outliers_removed.append(point)
    return outliers_removed


def k_means(points, k=3, max_iter=100):
    centroids = random.sample(points, k)

    for _ in range(max_iter):
        clusters = [[] for _ in range(k)]

        for point in points:
            distances = [euclidean_distance(point, c) for c in centroids]
            closest = distances.index(min(distances))
            clusters[closest].append(point)

        new_centroids = []
        for cluster in clusters:
            if cluster:
                avg_x = sum(p[0] for p in cluster) / len(cluster)
                avg_y = sum(p[1] for p in cluster) / len(cluster)
                new_centroids.append([avg_x, avg_y])
            else:
                new_centroids.append(centroids[clusters.index(cluster)])

        if new_centroids == centroids:
            break
        centroids = new_centroids

    return clusters


# Основной процесс
points = read_points('1.txt')
K = 0.5  # Порог для аномалий (можно настроить)
filtered_points = remove_outliers(points, K)
clusters = k_means(filtered_points, k=3)

# Вывод результата
for i, cluster in enumerate(clusters):
    print(f"Cluster {i + 1}: {cluster}")

# Если нужно вернуть аномалии отдельно:
outliers = [p for p in points if p not in filtered_points]
print(f"Anomalies: {outliers}")
print(f"Anomalies: {len(outliers)}")