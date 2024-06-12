#Задание 24.
#найти  макс. длину, где пара DE (в указаном порядке)
#есть 240 раз.
s = open('24.txt').readline()
s = s.split('DE')
mx_ln = 0
for x in range(len(s) - 240):
    ln = 0
    for y in range(0, 241):
        ln += len(s[x + y])
    mx_ln = max(mx_ln, ln + 480) # Еще 240 пар DE - это 480 символов
print(mx_ln)