import ipaddress
ct = 0
for x in ipaddress.ip_network('151.192.0.0/255.224.0.0', False):
    x = bin(int(x))[2:]
    if x.count('0') == x.count('1'):
        ct += 1
print(ct)