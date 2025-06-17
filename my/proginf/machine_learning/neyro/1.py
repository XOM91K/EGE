import math

# Линейная регрессия
def predict_grade(hours, tasks):
    w0, w1, w2 = 2, 1.5, 0.5
    return w0 + w1 * hours + w2 * tasks

# Нейрон с нелинейностью
def neuron_grade(hours, tasks):
    z = predict_grade(hours, tasks)
    return 1 / (1 + math.exp(-z))  # Сигмоида

# Пример
print("Линейная модель:", predict_grade(1, 1))  # 11.5
print("Нейрон:", neuron_grade(1, 1))           # ≈1.0 (5+)