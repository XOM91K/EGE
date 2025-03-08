import ipaddress
o = []
for i in range(1, 9):
    o.append((2 ** i) - 1)
ct = 0
for x in ipaddress.ip_network('139.75.100.0/255.255.252.0', False):
    x = bin(int(x))[2:].zfill(32)
    if int(x[-8:], 2) in o:
        ct += 1
print(ct)