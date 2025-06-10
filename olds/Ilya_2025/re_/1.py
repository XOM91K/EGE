import re
#Символьный класс
#Квантификаторы
s = 'Привет three two one SIX у1l как дела у 123 321 999 6444 12 меня Все хорошо как САМ поживаешь'
m = re.findall(r"\b\S{5}\b", s)
# \d - любая цифра
# \D - любая НЕ цифра
# \s - любой пробельный символ
# \S - любой НЕ пробельный символ
# \w - символ слова [A-Za-zА-Яа-я0-9]
# \W - символ НЕ слова
# \b - слово целиком
# | - или
print(m)

print('ok')
print('ok')
print('ok')
print('ok')
print('ok')
print('ok')
print('ok')
print('ok')
print('ok')
print('ok')
print('ok')