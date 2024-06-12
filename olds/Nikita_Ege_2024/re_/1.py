import re
s = 'Еда,1 еду, 33333п1313123123 еда, Еду,1239 Еды,  ёда 5123 еда 441234 333 \n \n \t \t \r \r '
m = re.findall(r"еда", s)
print(m)
#Символьный класс []
m = re.findall(r"[еЕ]да", s)
print(m)
m = re.findall(r"[еЕ]д[ыау]", s)
print(m)
m = re.findall(r"[5-9][5-9]", s)
print(m)
m = re.findall(r"\d\d", s) #\d - любая цифра (d - digit)
print(m)
m = re.findall(r"\w\w\w", s) #\w - любой символ слова (w - word)
print(m)
m = re.findall(r"\s", s) #\s - любой пробельный символ (s - space)
print(m)
#Квантификаторы {}
#по умолчанию поиск "мажорный"
#есть поиск "минорный" можно задать знаком "?" справа
m = re.findall(r"\d{2,4}?", s)
print(m)
# * от 0 до бесконечности символов
# + от 1 до бесконечности символов
# ? от 0 до 1
m = re.findall(r"\w+", s)
print(m)
#33333п1313123123
m = re.findall(r"\d+\w?\d+", s)
print(m)
#Объединяющие сохраняющие и НЕсохраняющие скобки
# .  - любой символ кроме символа \n
s = '<div class="taskType"><img class="taskTypeIcon" src= "img/Task2.png" '
m = re.findall(r"src\s?=\s?\"(.+)\"", s) # ( ) - сохраняющие
s = 'ASIDOASHDASOIH123123ASUGASUIDAGSDIA123123123ASUDASGDIUASDGI'
m = re.findall(r"(?:123)+", s) # (?: ) - НЕсохраняющие
print(m)
