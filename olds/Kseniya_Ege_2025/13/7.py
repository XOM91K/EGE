import ipaddress
d = []
for x in ipaddress.ip_network('135.221.128.0/255.255.128.0'):
    x = bin(int(x))[2:].zfill(32)
    d.append(x.count('1'))
print(min(d))