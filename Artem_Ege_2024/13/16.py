import ipaddress
ct = 0
for x in ipaddress.ip_network('212.170.112.0/255.255.240.0', False):
    x = bin(int(x))[2:]
    if x.count('1') != x.count('0'):
        ct += 1
print(ct)