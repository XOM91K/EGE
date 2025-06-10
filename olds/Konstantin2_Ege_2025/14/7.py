for x in range(0, 100):
    d = 81 ** 20 - 9 ** x + 50
    s = ''
    while d > 0:
        s += str(d % 9)
        d //= 9
    s = s[::-1]
    if sum(map(int, s)) == 138:
        print(x)
# # s = '129837123293612921639'
# # print(s.count('1') + s.count('2') * 2 + s.count('3') * 3 + s.count('4') * 4 + s.count('5') * 5 + s.count('6') * 6 + s.count('7') * 7 + s.count('8') * 8 + s.count('9') * 9)
# # print(sum(map(int, s)))
