from PIL import Image
import numpy as np
# # Изменение размера и преобразование в ч/б
# for x in range(1, 6):
#     img = Image.open(f"c0{x}.png").resize((28, 28)).convert('L')
#     img.save(f"c00{x}.png")

# img = Image.open(f"test0.png").resize((28, 28)).convert('L')
# img.save(f"test00.png")


#Шаг 2: Преобразование в пиксели
def image_to_pixels(image_path):
    img = Image.open(image_path).convert('L')  # 'L' — чёрно-белый режим
    pixels = np.array(img).flatten()  # Преобразуем в 1D-массив
    return pixels

X = []
y = []

# Загрузка "0"
for i in range(1, 6):
    X.append(image_to_pixels(f"c00{i}.png"))
    y.append(0)

# Загрузка "1"
for i in range(1, 6):
    X.append(image_to_pixels(f"c1{i}.png"))
    y.append(1)

X = np.array(X)
y = np.array(y)

#3. Обучение модели
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# Проверка на одной из "единиц"
test_image = image_to_pixels("test00.png")
prediction = model.predict([test_image])  # Ожидаем: 1
print(prediction)