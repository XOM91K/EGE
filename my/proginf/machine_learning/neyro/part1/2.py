import numpy as np

# Данные (площади 1-комн. квартир и цены в рублях)
X = np.array([30, 35, 40, 45])  # Площади квартир
y_true = np.array([9_000_000, 10_500_000, 12_000_000, 13_500_000])  # Цены

# Нормализуем данные для устойчивости обучения
# (Слишком большие числа (миллионы) могут вызвать переполнение, медленную сходимость.
X_norm = (X - np.mean(X)) / np.std(X)
y_norm = (y_true - np.mean(y_true)) / np.std(y_true)

# Инициализация
w = 0.1
learning_rate = 0.01
epochs = 50

for epoch in range(epochs):
    # Forward pass
    y_pred = X_norm * w

    # MSE и градиент
    mse = np.mean((y_pred - y_norm) ** 2)
    gradient = 2 * np.mean(X_norm * (y_pred - y_norm))

    # Обновление веса
    w -= learning_rate * gradient

    print(f"Epoch {epoch}: w = {w:.4f}, MSE = {mse:.4f}")

w = 0.6722 * (np.std(y_true) / np.std(X))
print(w)
