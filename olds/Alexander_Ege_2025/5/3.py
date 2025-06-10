d = 123128932
s = ''
while d > 0:
    s = s + str(d % 3)
    d = d // 3
s = s[::-1]
print(s)

# s = 'РАДУГА'
# print(s[::-1])