s = open('18.txt').readline()
l = 0
r = -1
ct = 0
while l != len(s) // 2 - 1:
    if s[l] == s[r]:
        ct += 1
    l += 1
    r -= 1
print(ct)