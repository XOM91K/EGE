# В текстовом файле k7.txt находится
# цепочка из символов латинского алфавита
# A, B, C длиной не более 106 символов.
# Найдите длину самой длинной подцепочки,
# состоящей из символов C.
s = open('1.txt').readline()
# k = 1    #1-й способ решения
# while 'C' * k in s:
#     k += 1
ct = 0 #2-й способ решения
mx = 0
for i in range(len(s)):
    if s[i] == 'C':
        ct += 1
    else:
        mx = max(mx, ct)
        ct = 0
print(mx)