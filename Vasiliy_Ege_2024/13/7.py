import ipaddress
ct = 0
#Сколько в этой сети IP-адресов, у которых
# в двоичной записи IP-адреса имеется сочетание трех подряд идущих единиц?
for x in ipaddress.ip_network('202.75.38.152/255.255.255.248', False):
    x = f'{x:b}'
    if '111' in x:
        ct += 1
print(ct)