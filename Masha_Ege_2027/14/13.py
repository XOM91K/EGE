# import string
# print(string.ascii_lowercase)
# for x in '0123456789QAZWSXEDCRFVTGBYHNUJMIKOLP@':
#     for y in '0123456789QAZWSXEDCRFVTGBYHNUJMIKOLP@':
#         c1 = int(f'21{x}457{y}9', 37)
#         c2 = int(f'{x}{y}', 37)
#         if c1 % 36 == 0:
#             print(c2)
for x in range(37):
    for y in range(37):
        c = 2 * 37 ** 7 + 1 * 37 ** 6 + x * 37 ** 5 + 4 * 37 ** 4 + 5 * 37 ** 3 + 7 * 37 ** 2 + y * 37 ** 1 + 9 * 37 ** 0
        if c % 36 == 0:
            print(x * 37 + y)