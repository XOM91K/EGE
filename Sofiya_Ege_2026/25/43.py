# # Напишите программу, которая перебирает целые числа, большие 6 300 000, в порядке
# # возрастания и ищет среди них числа, представимые в виде произведения ровно трёх
# # простых множителей, необязательно различных, каждый из которых содержит в своей
# # записи хотя бы одну цифру 3 или 4. В ответе запишите первые пять чисел в порядке
# # возрастания, справа от каждого числа запишите его наибольший простой делитель.
# # 6300051 2503
# # 6300057 39623
# # 6300069 1543
# # 6300087 9013
# # 6300101 4153
# def is_prime(d):
#     for x in range(2, int(d ** 0.5) + 1):
#         if d % x == 0:
#             return False
#     return d > 1
#
#
# def dels(d):
#     l = []
#     for x in range(1, int(d ** 0.5) + 1):
#         if d % x == 0:
#             if is_prime(x) and ((str(x).count('3')) >= 1 or (str(x).count('4')) >= 1):
#                 l.append(x)
#             if is_prime(d // x) and ((str(d // x).count('3')) >= 1 or (str(d // x).count('4')) >= 1):
#                 l.append(d // x)
#     return sorted(l)
#
#
# for x in range(6_300_001, 10 ** 7):
#     l = dels(x)
#     if (len(l) == 3 and l[0] * l[1] * l[2] == x):
#         print(x, max(l))

def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
def dels(d):
    l = []
    x = 2
    while x * x <= d:
        while d % x == 0:
            l.append(x)
            d //= x
            if len(l) > 3:
                return l
        x += 1
    if d > 1:
        l.append(d)

    return l
print(dels(5_000_012)) # <= пример как будет разложено число
ct = 0
for x in range(5_000_001, 10 ** 7):
    l = dels(x)
    if len(l) == 3 and all(str(k).count('2') == 1 for k in l):
        print(x, max(l))
        ct += 1

        if ct == 5:
            break