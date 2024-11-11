s = 'ГУСЬ'
print(s.count('РИ'))
print(s.replace('О', '@', 5))
print(s.index('С'))
print(s.zfill(10))

print(bin(5)[2:]) # перевод в 2-ую
print(oct(15)[2:]) #перевод в 8-ую
print(hex(35)[2:]) #перевод в 16-ую

print(int('23', 16)) #перевод в 10-ую из какой-то

s = 'КУКУШКА'
print(s[4:7])



s = 'ЗАРАЗА'
s = s.replace('А', '@')
print(s)


R = '10100011'
# 10100 10 11
ind = R.rindex('0')
R = R[:ind] + R[:2] + R[ind + 1:]
print(R)