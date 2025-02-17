import itertools
k = 0
for x in itertools.product(sorted('ТБДЦЭЕКНЧ'), repeat=6):
    x = ''.join(x)
    k += 1
    if k % 2 == 0 and x[0] != 'Н' and x[-1] != 'Н' and x.count('Е') >= 3:
        print(k, x)
# d = 'ПРИВЕТ'
# print(sorted(d))

# for x in itertools.permutations('ЙОД', 3):
#     print(x)

# s = '123' #str
# t = ('1', '2', '3') #tuple
# l = ['1', '2', '3'] #list
# l[1] = 1000
# #t[1] = 1000
# #s[1] = '9'
# print(s[0], t[0], l[0], l[1])
# print(s.__sizeof__()) #dunder-метод магический метод
# print(t.__sizeof__())
# print(l.__sizeof__())