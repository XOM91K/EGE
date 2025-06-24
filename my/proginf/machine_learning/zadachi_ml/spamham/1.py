import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# 1. Загрузка с обработкой ошибок

data = []
with open('spam.csv', 'r', encoding='latin-1') as f:
    for line in f:
        parts = line.strip().split(',', 1)
        if len(parts) == 2:
            data.append(parts)
df = pd.DataFrame(data[1:], columns=['label', 'text'])  # Пропускаем заголовок

# 2. Тщательная очистка данных
# Удаляем строки с пустым текстом или меткой
df = df.dropna(subset=['text', 'label'])

# Удаляем строки, где метка не 'spam' или 'ham'
valid_labels = {'spam', 'ham'}
df = df[df['label'].isin(valid_labels)]

# Преобразуем метки в числовой формат (0 - ham, 1 - spam)
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# 3. Создание и обучение модели
if len(df) > 0:  # Проверяем, что данные остались
    model = make_pipeline(
        TfidfVectorizer(stop_words='english'),
        MultinomialNB()
    )

    X = df['text']
    y = df['label']

    model.fit(X, y)

    # 4. Проверка
    test_messages = [
        "Free entry in 2 a weekly comp",
        "Hey, shall we meet tomorrow?",
        "WINNER!! Claim your prize now!",
        "Hi, can we reschedule our meeting?",
        "Good stuff, will do.",
        "Sindu got job in birla soft ..",
        "Ur ringtone service has changed!"
    ]

    print("Результаты проверки:")
    for msg in test_messages:
        prediction = model.predict([msg])[0]
        print(f"{msg[:40]}... -> {'SPAM' if prediction == 1 else 'HAM'} ")
else:
    print("Нет данных для обучения после очистки!")