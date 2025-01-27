# for n in range(1,100):
#     s = '>' + '0'*39 + '1'*n + '2'*39
#     while '>1' in s or '>2' in s or '>0' in s:
#         if '>1' in s:
#             s = s.replace('>1','22>', 1)
#         if '>2' in s:
#             s = s.replace('>2','2>', 1)
#         if '>0' in s:
#             s = s.replace('>0','1>', 1)
#     print(n, s.count('1') + s.count('2') * 2)

s = '1289316239216291004482947129481461249824612948126'
print(s.count('1') + s.count('2') * 2 + s.count('3') * 3 + s.count('4') * 4 + s.count('5') * 5 + s.count('6') * 6 + s.count('7') * 7 + s.count('8') * 8 + s.count('9') * 9)
print(sum(map(int, s))) #summapints сумапинтс