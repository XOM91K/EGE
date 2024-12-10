import ipaddress
for x in ipaddress.ip_network('135.221.128.0/255.255.128.0', 0):
    x = bin(int(x))[2:].zfill(32)
    print(x.count('1'))