# l = [1, 2, 2, 3]
# t = (1, 2, 2, 3)
# s = {1, 2, 2, 3}
# print(l, t, s)
# s = 'abracadabra'
# print(list(s).__sizeof__())
# print(tuple(s))
# print(set(s).__sizeof__())
# s = {4, 1, 2}
# s.add(10)
# s.remove(2)
# print(s)
# a = {3, 4, 5}
# b = {5, 10, 15}
# print(a | b) #      |    &
# print(a & b)
# s = "The Zen of PythonBeautiful is better than ugly.Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.Sparse is better than dense.Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.Errors should never pass silently.Unless explicitly silenced.In the face of ambiguity, refuse the temptation to guess.There should be one-- and preferably only one --obvious way to do it.Although that way may not be obvious at first unless you're Dutch.Now is better than never.Although never is often better than *right* now.If the implementation is hard to explain, it's a bad idea.If the implementation is easy to explain, it may be a good idea.Namespaces are one honking great idea -- let's do more of those!"
# print(len(set(s)))
a = input("Введите первую строку: ")
b = input("Введите вторую строку: ")

a_set, b_set = set(a), set(b) # используем множественное присваивание

a_and_b = a_set & b_set

print(a_and_b)