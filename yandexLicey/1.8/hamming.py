def hamming(n):
    ham = [1] * n
    p2, p3, p5 = 0, 0, 0
    for i in range(1, n):
        ham[i] = min(ham[p2] * 2, ham[p3] * 3, ham[p5] * 5)
        if ham[i] == ham[p2] * 2:
            p2 += 1
        if ham[i] == ham[p3] * 3:
            p3 += 1
        if ham[i] == ham[p5] * 5:
            p5 += 1
    return ham[n - 1]


print(hamming(int(input()) + 1))
