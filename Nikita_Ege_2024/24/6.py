import string
# Текстовый файл состоит не более чем из 10^6
# заглавных латинских букв (A..Z).
# Текст разбит на строки различной длины.
# Определите количество строк, в которых встречается комбинация A*R,
# где звёздочка обозначает любой символ.
s = open(r'C:\Users\Zarif\Downloads\24_618_1.txt').readlines()
ct = 0
for x in s:
    for y in string.ascii_uppercase:
        if 'A' + y + 'R' in x:
            ct += 1
            break
print(ct)