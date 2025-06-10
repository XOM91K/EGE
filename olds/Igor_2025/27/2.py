#https://examinf.ru/tasks/189
l = [int(x) for x in open(r'C:\Users\Zarif\Downloads\189_2 (1).txt')]
A = sorted(l[:len(l) // 2])
B = sorted(l[len(l) // 2:])
print(len(A))
print(len(B))
i = j = 0
mn_r = 10 ** 10
curr = 10 ** 10
while i != len(A) - 1 or j != len(B) - 1:
    curr = abs(A[i] - B[j])
    mn_r = min(mn_r, curr)
    if A[i] > B[j]:
        if j < len(B) - 1:
            j += 1
        elif i < len(A) - 1:
            i += 1
        else:
            break
    else:
        if i < len(A) - 1:
            i += 1
        elif j < len(B) - 1:
            j += 1
        else:
            break
print(i, j)
print(mn_r)