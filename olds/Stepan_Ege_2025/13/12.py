import ipaddress
ct = 0
for x in ipaddress.ip_network('5.2.5.0/255.255.0.0', False):
    d = bin(int(x))[2:].zfill(32)
    if d.count('0') % 25 == 0:
        ct += 1
print(ct)