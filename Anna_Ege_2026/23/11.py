def f(s, k, p):
    if s > k or p[:1] == 'A' or p[:1] == 'C':
        return 0
    if s == k and p[-1] not in 'AC':
        return 1
    return f(s + 5, k, p + 'A') + f(s + 10, k, p + 'B') + f(s * 3, k, p + 'C')
print(f(5, 165, ''))