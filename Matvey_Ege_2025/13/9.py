import ipaddress
ct = 0
for i in list(ipaddress.ip_network('111.194.0.0/255.254.0.0', 0))[1:-1]:
    i = bin(int(i))[2:].zfill(32)
    if (i.count('1') - i.count('0')) % 2 == 0:
        ct += 1
print(ct)