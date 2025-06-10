s = input()
floor = [0] * ((len(s) + 1) * 2 + 1)
floor[len(s) + 1] = 1
ind = len(s) + 1
k = 0
while k != len(s):
    if s[k] == '1':
        ind += 1
        floor[ind] = 1
    elif s[k] == '2':
        ind -= 1
        floor[ind] = 1
    k += 1
print(floor.count(1))