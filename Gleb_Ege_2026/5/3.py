for N in range(1, 10000):
    R = bin(N)[2:]
    if R.count('1') % 2 != 0:
        R = R + '11'
    else:
        R = '11' + R
    R = int(R, 2)
    if R > 102:
        print(N)


# print(2 / 3)
# print(2 // 3) #деление нацело
# print(14 // 4)
# print(19 // 10)
# print(5 // 5)
# #----
# print('---------')
# print(3 % 2) #деление по остатку
# print(7 % 3)
# print(19 % 15)
# print(4 % 2)
# print('------')
# print(5 % 2) #1
# print(7 % 2) #1
# print(111 % 2) #1
# print(6 % 2)#0
# print(88 % 2)#0
# print(1195 % 2)#1
# print(672 % 2)#0
#st = 'Hello'
# st.index('l') - находит индекс элемента слева
# st.rindex('l') находит индекс элемента справа