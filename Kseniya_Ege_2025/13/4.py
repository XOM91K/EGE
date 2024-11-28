import ipaddress
ct = 0
for x in ipaddress.ip_network('235.53.0.0/255.255.224.0', False):
    x = bin(int(x))[2:].zfill(32)
    if x.count('1') % 5 == 0:
        if x[-3:] == '110':
            ct += 1
print(ct)