#задача из ЕГКР
import ipaddress
ct = 0
for x in ipaddress.ip_network('192.168.32.96/255.255.255.224', False):
    a = f'{x:b}'
    b = bin(int(x))[2:]
    if a.count('1') % 2 == 0:
        ct += 1
print(ct)