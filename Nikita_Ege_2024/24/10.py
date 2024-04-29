#https://examinf.ru/ege/task.php?num=628
s = open(r'C:\Users\Zarif\Downloads\24_627_1 (1).txt').readlines()
sl = []
import string
alf = string.ascii_uppercase
k = 1
for x in alf:
    for y in s:
        while x * k in y:
            sl.append([k, y.count(x), x])
            k += 1
            if x * k not in y:
                k -= 1
                break
print(sl)