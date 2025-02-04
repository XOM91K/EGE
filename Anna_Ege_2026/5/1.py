l = []
for N in range(1, 10000):
    R = bin(N)[2:]
    if N % 3 == 0:
        R += R[-3:]
    else:
        R += bin(N % 3 * 3)[2:]
    R = int(R, 2)
    if R < 170:
        l.append(R)
print(max(l))
# s = 'red'
# s += 'no'
# print(s)
# s = 'СОЛНЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫШКО'
# #print(s[start_index:finish_index:step])
# print(s[:1]) #срез
# print(s[0]) #взятие элемента по индексу
# print(s[5:])
# print(s[-3:])