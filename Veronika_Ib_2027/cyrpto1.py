l = [10, 44, 196, 247, 142, 190, 2, 122, 66, 49, 204, 207, 148, 188, 95, 124, 54, 122, 213, 234, 152, 246]
for x in range(0, len(l), 2):
    r = l[x]
    l[x] = l[x + 1]
    l[x + 1] = r
print(l)
BASE = 90
STEP = 31

for x in range(len(l)):
    print(chr(l[x] ^ ((BASE + x * STEP) % 256)), end ='')