# # # l = [1, 2, 3, 99]
# # # g = max(l)
# # # print(g)
# # # print(max(l))
# # # print(99)
# # def sadasdsadsadasdsada(d):
# #     if int(d) % 2 == 0:
# #         return 'Четное'
# #     else:
# #         return 'Нечетное'
# # d = '55 33 1 4 9'
# # # print(list(map(int, d.split())))
# # print(list(map(sadasdsadsadasdsada, d.split())))
# # # Анонимные функции (lambda-функции)
# # print(list(map(lambda d: 'Четное' if int(d) % 2 == 0 else 'Нечетное', d.split())))
# # print(chet_nechet(5))
# # s = 'abracadabra'
# # print(set(s))
# import string
# def is_pangram(s):
#     s = s.lower()
#     for x in s:
#         if x not in string.ascii_lowercase:
#             s = s.replace(x, '')
#     if len(set(s)) == 26:
#         return True
#     return False

# import turtle
# turtle.forward(100)
# turtle.shape('square')
# turtle.done()