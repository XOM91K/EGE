import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score  # Добавляем этот импорт

train = pd.read_csv('train.csv')  # Данные для обучения
test = pd.read_csv('test.csv')    # Данные для теста (без Survived)
gender_subm = pd.read_csv('gender_submission.csv')

# print(train.groupby('Sex')['Survived'].mean())
# print(train.groupby('Pclass')['Survived'].mean())
# print(sns.boxplot(x='Survived', y='Age', data=train))
# print(train.groupby('Pclass')['Survived'].mean())
train_clean = train.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)
test_clean = test.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)
print(train_clean.columns)
# Index(['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare',
#        'Embarked'],
#       dtype='object')
print(train_clean.isnull().sum())
# Survived      0
# Pclass        0
# Sex           0
# Age         177  # Нужно заполнить
# SibSp         0
# Parch         0
# Fare          0
# Embarked      2  # Нужно заполнить

# Заполнение пропусков:
# Age: Заменим медианным возрастом.
# Embarked: Заменим самым частым значением (S).

# Заполняем пропуски
train_clean['Age'].fillna(train_clean['Age'].median(), inplace=True)
train_clean['Embarked'].fillna('S', inplace=True)

# Проверяем
print(train_clean.isnull().sum())
# dtype: int64
# Survived    0
# Pclass      0
# Sex         0
# Age         0
# SibSp       0
# Parch       0
# Fare        0
# Embarked    0



#4. Преобразование категориальных признаков
# Модели не работают с текстом, поэтому преобразуем:
# Sex → male=0, female=1
# Embarked → S=0, C=1, Q=2
train_clean['Sex'] = train_clean['Sex'].map({'male': 0, 'female': 1})
train_clean['Embarked'] = train_clean['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

# Аналогично для test_clean
test_clean['Sex'] = test_clean['Sex'].map({'male': 0, 'female': 1})
test_clean['Embarked'] = test_clean['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
test_clean['Age'].fillna(test_clean['Age'].median(), inplace=True)
test_clean['Fare'].fillna(test_clean['Fare'].median(), inplace=True)



# X — признаки, y — целевая переменная (Survived)
X = train_clean.drop('Survived', axis=1)
y = train_clean['Survived']


#5. Разделение данных на обучающую и тестовую выборки
# Разделяем данные: 80% — обучение, 20% — валидация
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Размеры данных:")

print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)


#6. Обучение модели (Decision Tree)
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)
# Предсказание на валидационной выборке
y_pred = model.predict(X_test)
# Оценка точности
print("Accuracy:", accuracy_score(y_test, y_pred))


# 7. Важность признаков
# Посмотрим, какие признаки модель сочла наиболее важными:
import matplotlib.pyplot as plt

# Сортируем признаки по важности
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': model.feature_importances_
}).sort_values('Importance', ascending=False)

# График
plt.barh(feature_importance['Feature'], feature_importance['Importance'])
plt.title('Важность признаков')
plt.show()


# 8. Предсказание для тестовых данных (test.csv)
# Предсказываем Survived для test_clean
test_predictions = model.predict(test_clean)

# Создаём файл для отправки на Kaggle
submission = pd.DataFrame({
    'PassengerId': test['PassengerId'],
    'Survived': test_predictions
})
submission.to_csv('submission.csv', index=False)