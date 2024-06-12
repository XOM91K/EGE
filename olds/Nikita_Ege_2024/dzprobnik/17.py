l = [int(x) for x in open('17.txt')]
otv = 0
mx = 0
for i in range(0, len(l)-3):
    if (abs(l[i]) % 100 == 13 and abs(l[i+3]) % 100 != 13) or (abs(l[i+3]) % 100 == 13 and abs(l[i]) % 100 != 13):
        otv += 1
        mx = max(mx, l[i] + l[i+3])
print(otv, mx)