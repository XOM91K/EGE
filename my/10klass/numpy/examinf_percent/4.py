# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup
# import re
# import time
#
# # Настройка Selenium с автоматической установкой ChromeDriver
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Режим без графического интерфейса
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--window-size=1920,1080")
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=chrome_options)
# # Загрузка страницы
# sr = 0
# for y in range(1, 6):
#     url = f"https://examinf.ru/tasks/ofType/ege/{y}"
#     driver.get(url)
#     time.sleep(3)  # время ожидания для полной загрузки
#     # Получаем HTML после выполнения JS
#     html = driver.page_source
#     soup = BeautifulSoup(html, 'html.parser')
#     # Словарь для хранения результатов
#     tasks_complexity = {}
#     # Находим все блоки с заданиями (они имеют id в формате "task-{номер}")
#     task_blocks = soup.find_all(id=re.compile(r'task-\d+'))
#     for block in task_blocks:
#         # Извлекаем ID задания
#         task_id = block['id'].split('-')[1]
#         # Извлекаем "сложность"
#         complexity_tag = block.find('p', class_='taskComplexity-text')
#         if complexity_tag:
#             match = re.search(r'(\d+)%', complexity_tag.text)
#             if match:
#                 tasks_complexity[task_id] = int(match.group(1))
#     # Вывод результатов
#     if tasks_complexity:
#         # Средняя сложность
#         avg = sum(tasks_complexity.values()) / len(tasks_complexity)
#         sr += avg
#     else:
#         print("Не удалось найти данные о сложности.")
# sr = sr / 5


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re
import time
def get_sr():
    # Настройка Selenium с автоматической установкой ChromeDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Режим без графического интерфейса
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    # Загрузка страницы
    sr = 0
    for y in range(1, 6):
        url = f"https://examinf.ru/tasks/ofType/ege/{y}"
        driver.get(url)
        time.sleep(3)  # время ожидания для полной загрузки
        # Получаем HTML после выполнения JS
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        # Словарь для хранения результатов
        tasks_complexity = {}
        # Находим все блоки с заданиями (они имеют id в формате "task-{номер}")
        task_blocks = soup.find_all(id=re.compile(r'task-\d+'))
        for block in task_blocks:
            # Извлекаем ID задания
            task_id = block['id'].split('-')[1]
            # Извлекаем "сложность"
            complexity_tag = block.find('p', class_='taskComplexity-text')
            if complexity_tag:
                match = re.search(r'(\d+)%', complexity_tag.text)
                if match:
                    tasks_complexity[task_id] = int(match.group(1))
        # Вывод результатов
        if tasks_complexity:
            # Средняя сложность
            avg = sum(tasks_complexity.values()) / len(tasks_complexity)
            sr += avg
        else:
            print("Не удалось найти данные о сложности.")
    return sr / 5
sr2 = get_sr()
if sr2 == sr:
    print('Код верный')
else:
    print('Код неверный')