a = int(input())
b = int(input())
for i in range(b // 25 + 1):
    for j in range((b - i * 25) // 10 + 1):
        for k in range(((b - i * 25) - j * 10) // 7 + 1):
            if i * 25 + j * 10 + k * 7 == b and i + j + k == a:
                print(i, j, k, sep=' ')
            elif i * 25 + j * 10 + k * 7 > b or i + j + k > a:
                break
