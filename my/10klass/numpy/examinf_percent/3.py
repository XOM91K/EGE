# import requests
#
#
# def get_task_ids1(task_type):
#     """Получает список ID заданий указанного типа"""
#     url = f"https://examinf.ru/api/tasks/ids/ege/{task_type}/"
#     response = requests.get(url)
#     return response.json()["result"]
#
#
# def get_task_stats1(task_id):
#     """Получает статистику для конкретного задания"""
#     url = f"https://examinf.ru/api/task/{task_id}/additionalInfo/"
#     response = requests.get(url)
#     data = response.json()["result"]
#     return data['likeCount'], data['dislikeCount']
#
#
# def analyze_task_type1(task_type):
#     """Анализирует все задания указанного типа"""
#     task_ids = get_task_ids1(task_type)
#     total_likes = 0
#     total_dislikes = 0
#
#     for task_id in task_ids:
#         try:
#             likes, dislikes = get_task_stats1(task_id)
#             total_likes += likes
#             total_dislikes += dislikes
#         except:
#             continue
#
#     return total_likes, total_dislikes
#
#
# # Анализ заданий типа 5
# likes, dislikes = analyze_task_type1(5)
# # Вывод результатов (это будет проверять тестирующая система)
import json

import requests

url = "https://examinf.ru/api/task/4/additionalInfo/"
response = requests.get(url)  # Отправляем GET-запрос

if response.status_code == 200:
    data = response.json()  # Парсим JSON
    print(data)
else:
    print("Ошибка:", response.status_code)


def get_task_ids(task_type):
    url = f"https://examinf.ru/api/tasks/ids/ege/{task_type}/"
    response = requests.get(url)
    return response.json()["result"]  # Например, [17, 42, 1337]


def get_task_stats(task_id):
    url = f"https://examinf.ru/api/task/{task_id}/additionalInfo/"
    data = requests.get(url).json()
    return data['result']['likeCount'], data['result']['dislikeCount']


task_ids = get_task_ids(5)  # Тип задания №5
total_likes, total_dislikes = 0, 0

for task_id in task_ids:
    likes, dislikes = get_task_stats(task_id)
    total_likes += likes
    total_dislikes += dislikes

print(f"Лайков: {total_likes}, Дизлайков: {total_dislikes}")

response = requests.get(url)
if not response.ok:  # Проверяем статус 200-299
    print(f"Ошибка {response.status_code}")

try:
    data = response.json()
    likes = data['result']['likeCount']
except KeyError:
    print("В ответе API нет нужных полей")
except json.JSONDecodeError:
    print("Ответ не в формате JSON")