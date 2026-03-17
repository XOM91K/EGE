# s = "The Zen of PythonBeautiful is better than ugly.Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.Sparse is better than dense.Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.Errors should never pass silently.Unless explicitly silenced.In the face of ambiguity, refuse the temptation to guess.There should be one-- and preferably only one --obvious way to do it.Although that way may not be obvious at first unless you're Dutch.Now is better than never.Although never is often better than *right* now.If the implementation is hard to explain, it's a bad idea.If the implementation is easy to explain, it may be a good idea.Namespaces are one honking great idea -- let's do more of those!"
# print(len(set(s)))
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(id(a), id(b))
# a = [1, 2, 3]
# b = a
# a.append(100)
# print(a)
# print(b)
# b.append(-500)
# print(a)
# print(a is b)
# print('Четное' if 11 % 2 == 0 else 'Нечетное')
# l = []
# for i in range(1, 10):
#     if i % 2 == 0:
#         l.append(i)
# print(l)
# print([i ** 2 for i in range(1, 10) if i % 2 == 0])
# s = 'Привет мир! Привет, как дела?'
# print([x for x in s if x in 'аеоуыи'])
# s = 'apple banana apple orange banana two two one one two one yupi gh'.split()
# print(s)
# s2 = []
# for x in s:
#     if s.count(x) == 1:
#         s2.append(x)
# print(s2)

# for x in range(len(s)):
#     for y in range(len(s)):
#         if x != y:
#             if s[x] == s[y]:
#                 break
#     else:
#         print('Уникальное слово:', s[x])
# s = '1 2 3 4 5 6'
# s = list(map(int, s.split()))
# print(s)
# print('Четные:', [r for r in s if r % 2 == 0])
# print('Нечетные:', [r for r in s if r % 2 != 0])
# s = ['Никита', 'Мирослав', 'Ян']
# print(max(s, key=len))
# print(max(s, key=str))
# s = 'apple banana cherry'.replace('A', 'a').split()
# for x in s:
#     x = x.replace('a', '@', 1)
#     print(x, end=' ')

# поиндексовый перебор
# s = 'Helloasdioashdoiddhiosad'
# for x in range(len(s) - 1):
#     print(s[x] + s[x + 1])