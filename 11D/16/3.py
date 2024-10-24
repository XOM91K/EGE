import ipaddress
mn = 10 ** 10
for x in ipaddress.ip_network('135.221.128.0/255.255.128.0', False):
    print(x)
    x = bin(int(x))[2:].zfill(32)
    mn = min(mn, x.count('1'))
print(mn)
