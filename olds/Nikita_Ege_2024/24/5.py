import collections
#Текстовый файл содержит только заглавные
# буквы латинского алфавита (ABC…Z).
# Определите символ,
# который чаще всего встречается в файле сразу после буквы A.
s = open(r'C:\Users\Zarif\Downloads\24_616_1.txt').readline()
a = ''
s = s.split('A')
for x in s:
    if len(x) > 0:
        a += x[0]
print(collections.Counter(a).most_common()[0])
# sl = {}
# while s.find('A') != -1:
#     if s[s.find('A') + 1] not in sl:
#         sl[s[s.find('A') + 1]] = 0
#     sl[s[s.find('A') + 1]] += 1
#     s = s.replace('A', '#', 1)
#print(sl)