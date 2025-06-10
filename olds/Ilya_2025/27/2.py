l = [int(x) for x in open(r'C:\Users\Zarif\Downloads\27B_7603 (1).txt')]
mx_l = []
k = 1_000_000
for i in range(len(l) - 1):
    for j in range(i + k, len(l)):
        mx_l.append(l[i] + l[j])
print(max(mx_l))