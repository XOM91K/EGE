def prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
ct =0
import ipaddress
for x in ipaddress.ip_network('172.118.1.255/255.255.252.0',False).hosts():
    x = f'{x:b}'
    if prime(x.count('1')):
        ct += 1
print(ct)