import numpy as np
from annoy import AnnoyIndex
import matplotlib.pyplot as plt

# Данные: x, y, класс
data = [
    [3.9638064, 7.1285385, 1],
    [4.1852033, 6.1452368, 2],
    # ... (остальные точки из вашего примера)
    [3.7553337, 7.0652113, 3]
]

# Разделяем координаты и метки
points = np.array([point[:2] for point in data])
labels = np.array([point[2] for point in data])

# Параметры Annoy
dim = 2           # Размерность данных (x, y)
n_trees = 10      # Количество деревьев (больше → точнее, но медленнее)
k = 3             # Количество ближайших соседей для поиска

# Создаем индекс Annoy
index = AnnoyIndex(dim, 'euclidean')
for i, point in enumerate(points):
    index.add_item(i, point)
index.build(n_trees)

# Функция предсказания класса через k-NN
def predict_class(new_point, k):
    nearest_indices = index.get_nns_by_vector(new_point, k)
    nearest_labels = labels[nearest_indices]
    return np.bincount(nearest_labels).argmax()  # Самый частый класс

# Пример предсказания для новой точки
new_point = [3.8, 6.5]
predicted_class = predict_class(new_point, k)
print(f"Предсказанный класс для {new_point}: {predicted_class}")

# Визуализация
colors = {1: 'blue', 2: 'green', 3: 'red'}
plt.figure(figsize=(10, 6))
for i, point in enumerate(points):
    plt.scatter(point[0], point[1], color=colors[labels[i]], label=f'Class {labels[i]}' if i < 3 else "")
plt.scatter(new_point[0], new_point[1], color='black', marker='x', s=100, label='Новая точка')
plt.title('Классификация через Annoy')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid()
plt.show()