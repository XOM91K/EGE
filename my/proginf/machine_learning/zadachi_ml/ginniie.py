import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

# Генерация данных
np.random.seed(42)
X1 = np.random.rand(200) * 10
X2 = np.random.rand(200) * 10
y = np.where((X1 + X2 > 10) & (X1 * X2 < 30), 1, 0)  # Нелинейное разделение

# Добавим немного шума
y = np.where(np.random.rand(200) > 0.9, 1 - y, y)

# Визуализация
plt.scatter(X1, X2, c=y, cmap='coolwarm', edgecolors='k')
plt.xlabel("X1"), plt.ylabel("X2"), plt.title("Исходные данные")
plt.colorbar(label="Класс (0 или 1)")
plt.show()


tree = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)
tree.fit(np.column_stack((X1, X2)), y)
xx, yy = np.meshgrid(np.linspace(0, 10, 100), np.linspace(0, 10, 100))
Z = tree.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

# Визуализация
plt.contourf(xx, yy, Z, alpha=0.3, cmap='coolwarm')
plt.scatter(X1, X2, c=y, cmap='coolwarm', edgecolors='k')
plt.xlabel("X1"), plt.ylabel("X2"), plt.title("Разделяющая граница дерева")
plt.show()

