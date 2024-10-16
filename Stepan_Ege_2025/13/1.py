import ipaddress
ct = 0
for x in ipaddress.ip_network('192.168.32.160/255.255.255.240', False):
    x = bin(int(x))[2:].zfill(32)
    if x.count('0') > 21:
        ct += 1
print(ct)
