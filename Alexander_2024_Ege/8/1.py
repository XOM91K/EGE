# Сколько слов длины 5, начинающихся с
# гласной буквы, можно составить из букв
# Е, Г, Э? Каждая буква может входить в
# слово несколько раз. Слова не обязательно
# должны быть осмысленными словами русского языка.
import itertools
ct = 0
for x in itertools.product('ЕГЭ', repeat=5):
    x = ''.join(x)
    if x[0] in 'ЕЭ':
        ct += 1
print(ct)