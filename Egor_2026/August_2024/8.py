# 1 1 2 3 5 8 13 21 34 55
d = int(input())
fibo = [1, 1]
for x in range(2, d):
    fibo.append(fibo[x - 1] + fibo[x - 2])
    if fibo[-1] == d:
        print('1')
        print(x + 1)
        break
else:
    print('0')