import pandas as pd
from sklearn.tree import DecisionTreeClassifier


def predict_survival(pclass, age, sex, fare):
    # Данные уже загружены и предобработаны (чтобы упростить задачу)
    data = {
        'Pclass': [1, 1, 3, 2, 3, 1, 2, 3, 2, 1],
        'Age': [30, 45, 20, 19, 25, 50, 23, 18, 35, 40],
        'Sex': [0, 1, 1, 0, 1, 0, 1, 0, 1, 0],  # 0 = male, 1 = female
        'Fare': [50, 70, 10, 20, 15, 80, 30, 8, 40, 60],
        'Survived': [1, 1, 0, 0, 0, 1, 1, 0, 0, 1]
    }
    df = pd.DataFrame(data)

    X = df[['Pclass', 'Age', 'Sex', 'Fare']]
    y = df['Survived']

    model = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)
    model.fit(X, y)

    # Создаём DataFrame для предсказания с теми же именами признаков
    new_data = pd.DataFrame([[pclass, age, sex, fare]],
                            columns=['Pclass', 'Age', 'Sex', 'Fare'])

    prediction = model.predict(new_data)
    return prediction[0]  # 0 или 1


# Тестовые примеры
print(predict_survival(1, 30, 0, 50))  # Ожидается: 1
print(predict_survival(3, 20, 1, 10))  # Ожидается: 0
print(predict_survival(2, 19, 0, 20))  # Ожидается: 0
print(predict_survival(1, 77, 0, 20))  # Ожидается: 1
print(predict_survival(2, 33, 1, 20))  # Ожидается: 1