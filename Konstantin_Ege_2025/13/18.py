import ipaddress
ct = 0
for x in ipaddress.ip_network('172.16.192.0/255.255.192.0', False):
    x = bin(int(x))[2:].zfill(32)
    if x.count('1') % 5 != 0:
        ct += 1
        print(ct)