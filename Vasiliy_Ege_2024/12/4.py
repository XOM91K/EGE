# На вход приведённой выше программе
# поступает строка, начинающаяся с символа «>»,
# а затем n цифр «0», n цифр «1» и n цифр «2»,
# расположенных в произвольном порядке. Известно,
# что n > 40. Определите наименьшее значение n, при
# котором сумма числовых значений цифр строки, получившейся
# в результате выполнения
# программы, будет оканчиваться на 77.
for n in range(41, 100):
    s = '>' + '0' * n + '1' * n + '2' * n
    while '>1' in s or '>2' in s or ">0" in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '00>', 1)
        if '>0' in s:
            s = s.replace('>0', '11>', 1)
    s = s.replace('>', '1', 1)
    if (s.count('1') + s.count('2') * 2) % 100 == 77:
        print(n)