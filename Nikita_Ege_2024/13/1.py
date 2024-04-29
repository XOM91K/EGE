import ipaddress
ct = 0
for x in ipaddress.ip_network('192.168.32.160/255.255.255.240'):
    if f'{x:b}'.count('1') % 2 == 0:
        print(x)
        print(f'{x:b}')
        ct += 1
print(ct)