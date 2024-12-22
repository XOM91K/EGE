#https://examinf.ru/tasks/218
import ipaddress
ct = 0
for x in ipaddress.ip_network('192.168.32.160/255.255.255.240', 0):
    x = bin(int(x))[2:].zfill(32)
    if x.count('0') > 21:
        print(x)
        ct += 1
print(ct)