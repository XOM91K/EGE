# Дана программа для исполнителя Редактор:
#
# НАЧАЛО
# ПОКА нашлось (72) ИЛИ нашлось (522) ИЛИ нашлось (2222)
#   ЕСЛИ нашлось (72)
#     ТО заменить (72, 2)
#   КОНЕЦ ЕСЛИ
#   ЕСЛИ нашлось (522)
#     ТО заменить (522, 27)
#   КОНЕЦ ЕСЛИ
#   ЕСЛИ нашлось (2222)
#     ТО заменить (2222, 5)
#   КОНЕЦ ЕСЛИ
# КОНЕЦ ПОКА
# КОНЕЦ
#
# На вход приведённой выше программе поступает строка, начинающаяся с цифры «5», а затем содержащая n цифр «2» (3 < n < 10 000). Определите наименьшее значение n, при котором сумма цифр в строке, получившейся в результате выполнения программы, равна 63.
for n in range(4, 10000):
    s = '5' + '2' * n
    while '72' in s or '522' in s or '2222' in s:
        if '72' in s:
            s = s.replace('72', '2', 1)
        if '522' in s:
            s = s.replace('522', '27', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
    if sum((map(int,s))) == 63:
        print(n)