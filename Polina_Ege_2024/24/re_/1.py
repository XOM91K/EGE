import re
s = 'ЛЕСОПОЛОСА Еда,ЕДАЕДА еду, ЕДА 123 55 ЕДАЕДАЕДА ЛЕСФЫВЛОСА  УРАУРАУРА ЛЕСОЙЦУОСА ЛЕСОЗЩШОСА 99 66 1 1 9 665 100 773 099 Еду, ФЫВШЩРЦВШЩЙЦРВЙЦВРЙЦШВЩЦЙРВЩ еда, еда, еды ёёё one, two, six, apple, yellow, blue'
s = '<form name="stdform" action="gen.php" method="get" style="margin:0;padding:0 0 0 10px;">'
m = re.findall(r"еда", s)
# 1. Символьный класс []
m = re.findall(r"[Ее]д[ауы]", s)
m = re.findall(r"[а-яА-Яё][а-яА-Яё][а-яА-Яё]", s)
m = re.findall(r"[a-z][a-z][a-z]", s)
m = re.findall(r"[1-9][0-9]", s)
m = re.findall(r"\w\w\w", s) #\w (word) - \w - любой символ слова - аналог
# [а-яА-Яёa-zA-Z0-9]
m = re.findall(r"\d\d\d", s) #\d (digit) - \d - любой символ цифры
# 2. Квантификаторы {}
m = re.findall(r"\w{10}", s)
m = re.findall(r"\w{3,5}", s)
#по умолчанию поиск в регулярках - "мажорный"
m = re.findall(r"\w{3,5}?", s) # ? - это "минорный" поиск
# + поиск символов от 1 до бесконечности
# * поиск символов от 0 до бесконечности
# ? поиск символов от 0 до 1
m = re.findall(r"\w+", s)
m = re.findall(r"\w*", s)
m = re.findall(r"\w?", s)
# 3. Группирующие сохраняющие и НЕсохраняющие скобки ()
m = re.findall(r"(?:ЕДА)+|(?:УРА)+", s)
m = re.findall(r"action\s?=\s?\"\w+.php\"", s)
print(m)