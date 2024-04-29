# import ipaddress
# ct = 0
# for x in ipaddress.ip_network('192.168.32.160/255.255.255.240'):
#     d = ''.join([bin(int(g))[2:] for g in str(x).split('.')])
#     if d.count('1') % 2 == 0:
#         ct += 1
# print(ct)
import ipaddress
ct = 0
for x in ipaddress.ip_network('192.168.32.160/255.255.255.240'):
    d = f'{x:b}'
    if d.count('1') % 2 == 0:
        ct += 1
print(ct)