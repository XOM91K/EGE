a = []
import ipaddress
for x in ipaddress.ip_network('69.121.128.142/255.255.252.0', 0):
    x = bin(int(x))[2:].zfill(32)
    x = int(x, 2)
    print(x)