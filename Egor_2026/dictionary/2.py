s = 'Привет как дела у меня все ййййййййййййййййййййхорошо............'
#Ищет наибольше-встречающийся символ
sl = {}
for x in s:
    if x not in sl:
        sl[x] = 0
    sl[x] += 1
mx = 0
symbol = ''
for x in sl:
    if sl[x] > mx:
        mx = sl[x]
        symbol = x
print(symbol)