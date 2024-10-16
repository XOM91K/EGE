# Речной бой Школьный этап 2023/2024
n = int(input())
k = int(input())
if n % 2 == 0:
    print(n // k + (k - 1))
else:
    print(n // (k - 1) + (k - 1))
