ct = 0


def f(x):
    return (A % 35 == 0) and ((730 % x == 0) <= ((A % x != 0) <= (110 % x != 0)))

ct = 0
for A in range(1, 1001):
    if all(f(x) == 1 for x in range(1, 1001)):
        print(A)
        ct += 1
print(ct)