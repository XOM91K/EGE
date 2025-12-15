# int , str
# d = 10000
# print(d + 2)
# s = '5'
# print(s + '4')
####
#int
###
# d = 959
# print(d + 5)
# print(d - 4)
# print(d / 4)
# print(d * 9)
# print(d // 4)
# print(d % 4)
# print(17 % 15)
# print(9 % 5)
# print(8 % 4)
# print(9 // 5)
# str
# s = 'Hellasdsaddasapo'
#print(s[start_index:finish_index:step])
# print(s[::-2])
# print(s[::-1])
# print(s[-4:])
# print(s[:4])
# print(s[0:2])
# print(s[1])
# print(s[-1])
# print(s[-2])
# print(s)
# s = 'abracadabra'
# Функции
# print(len(s))
# Методы
# print(s.replace('ab', '%'))
# s = s.replace('a', '@')
# print(s)
# print(s.rindex('r'))
# print(s.index('r'))
# print(s.count('a'))
# print(s.count('ab'))

# Списки list
#l = [10, 12, 'hello', 7, 'a', [1, 2, 3]]

# print(l[2])
# print(l[-1][-1])
# l = ['Максим', 'Ян', 'Николай']
# print(max(l, key=len))
# print(max(l, key=str))
#l = [1, 50, -20, -23, 77, 2]
# Срезы
# print(l[::-1])
# print(l[:3])
# Функции
# print(sorted(l, reverse=True))
# print(sorted(l)[::-1])
# l = sorted(l)
#print(l)
# print(len(l))
# print(max(l))
# print(min(l))
# print(sum(l))
#
# l = [1, 50, -20, -23, 77, 2, 50]
# l = sorted(l, reverse=True)
# print(l)
# l.sort(reverse=True)
# # l = l[::-1]
# print(l)
# l.insert(2, 500)
# l.insert(-2, -200)
# # l.clear()
# print(l)
# l.remove(50)
# # l.pop(1)
# # del l[2]
# print(l.pop(3))
# print(l)
# print(l.count(50))
# print(l.index(50))
# l.append(500)
# l.append(500)
# print(l)
# d = 77
# # print(62 % 2)
# # print(123124 % 2 )
# # print(123123131118 % 2)
# if d % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')
# Тернарный условный оператор
# d = 77
# print('Четное' if d % 2 == 0 else 'Нечетное')
# d = 1293723912639123623938192129312
# print(len(str(d)))
# print(list(str(d)))
# s = 'Hello'
# print(s[2])
# s = list(s)
# print(s)
# print(s[2])
# s = 'red blue green'
# s = s.split()
# print(s[-1])
# d = ['ball', 'tv', 'table', 'asdasd', '12i122189']
# print('    '.join(d))
# for x in range(10):
#     print('Hello')
# print(list(range(10)))
# for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     print(x)
# ct = 0
# for x in range(2, 1001, 2):
#     ct += 1
#     print(x)
# print(ct)
# for x in range(10, -1, -1):
#     print(x)
d = 188
print(bin(d)[2:])
d = 12331
print(oct(d)[2:])
d = 12103
print(hex(d)[2:])

print(int('2f47', 16))
print(int('30053', 8))