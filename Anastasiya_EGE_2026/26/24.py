l = [int(x) for x in open('24.txt')]
N = sorted(l[:900])
M = sorted(l[900:])
ct = 0
indexes = []
for x in range(len(N)):
    for y in range(len(M)):
        if N[x] <= M[y] and y not in indexes:
            ct += 1
            print(N[x])
            indexes.append(y)
            break
print(ct)
print(M[-1])
# for x in N:
#     if x > 402:
#         print(x)