cnt = 0
import ipaddress
for A in range(256):
    can = True
    for i in ipaddress.ip_network("246.81.65." + str(A) + "/255.255.255.224", False):
        i = bin(int(i))[2:].zfill(32)
        if i[16:24].count("0") <= i[24:32].count("0"):
            can = False
    if can:
        cnt += 1
print(cnt)