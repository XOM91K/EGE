from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 1. Запуск браузера (Chrome)
driver = webdriver.Chrome()
# 2. Открытие страницы
driver.get("https://www.google.com")
# 3. Поиск поля ввода и ввод текста
search_box = driver.find_element(By.NAME, "q")  # Ищем поле поиска Google
search_box.send_keys("Selenium WebDriver" + Keys.RETURN)  # Вводим текст и нажимаем Enter
# 4. Ждём 3 секунды (для демонстрации)
import time
time.sleep(3)
# 5. Закрываем бразер
driver.quit()

