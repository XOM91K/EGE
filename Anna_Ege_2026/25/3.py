def dels(n: int) -> list:
    lst = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            if x % 2 != 0:
                lst.append(x)
            if (n // x) % 2 != 0:
                lst.append(n // x)
    return sorted(set(lst))
for x in range(18782, 18823):
    lst = dels(x)
    if len(lst) == 3:
        print(*lst)
