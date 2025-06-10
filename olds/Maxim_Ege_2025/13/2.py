import ipaddress
ct = 0
for x in ipaddress.ip_network('102.141.0.0/255.255.192.0', False):
    x = bin(int(x))[2:].zfill(32)
    if x.count('1') % 7 == 0 and x[-4:] == '1011':
        ct += 1
print(ct)