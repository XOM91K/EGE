import re
s = '<h1 class="header-text">Дневник.ру — <span class="header-text_gray">цифровая образовательная платформа, которая делает образование<br />в России качественным и доступным!</span></h1>'
m = re.findall(r'class="header-text">(.+?)<', s)
print(m)
#Сохраняющие и не сохраняющие объединяющие скобки
# мажорный поиск, минорный поиск