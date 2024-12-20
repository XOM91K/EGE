import ipaddress
ct = 0
print(ipaddress.ip_network('90.65.32.0/255.255.224.0', False))
for x in ipaddress.ip_network('90.65.32.0/255.255.224.0', False):
    x = bin(int(x))[2:].zfill(32)
    if x.count('1') == x.count('0'):
        ct += 1
print(ct)