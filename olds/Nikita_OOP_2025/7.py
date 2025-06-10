s = []
s_str = ''
# Напишите программу, выбирающую волшебные изменения.
# В файле darkness.txt записаны пары строк. Из каждой пары выберите слова, которые есть во второй строке, но нет в первой. Запишите их в исходном порядке в файл changes.txt. Слова в строках разделены пробелами.
# В задаче ничего не вводится и не выводится, все действия производятся с указанными файлами.

# ввод
# Once, when he was a child, the electricity went out
# Once upon a time he went a fairy road
# and his mother found and lit the last candle
# Mother went out and found the last apple
# This short hour, while the candle was burning
# was an hour of wonderful discoveries
# вывод
# Once upon time fairy road
# Mother went out apple
# an hour of wonderful discoveries

# ввод
# Mother and son sat together
# together with any friend and son
# strangely transformed sincerely wishing
# the strangely aliens wishing your world
# that the electricity would not turn on
# the hedgehog would turn back
# for as long as possible
# for a long time
#   вывод
# with any friend
# the aliens your world
# hedgehog back
# a time
with open('darkness.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    for i in range(1, len(data), 2):
        s.append([])
        d2 = data[i].strip().split()
        d1 = data[i - 1].strip().split()
        for j in d2:
            if j not in d1:
                s[-1].append(j)

for x in range(len(s)):
    s[x] = ' '.join(s[x])
with open('changes.txt', 'w', encoding='utf-8') as f_out:
    for y in s:
        f_out.write(y + '\n')