import ipaddress
ct = 0
for x in ipaddress.ip_network('10.128.0.0/255.255.192.0', 0):
    x = bin(int(x))[2:].zfill(32)
    if x.count('1') % 4 == 0:
        ct += 1
print(ct)