n = int(input()) #7
k = int(input()) #3
ct = 0
if n % k != 0:
    print(n // k + (k - 1) + 1)
else:
    print(n // k + (k - 1))