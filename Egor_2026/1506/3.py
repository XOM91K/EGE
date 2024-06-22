a = ['a', 'apple', 55, -100, 5.2, 'joker', True, False, [1, 2, 3]]
a = list(filter(lambda x: type(x) == str, a))
print(a)