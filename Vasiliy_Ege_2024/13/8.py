import ipaddress
ct = 0
#Сколько в этой сети IP-адресов, двоичная запись
# которых оканчивается на две единицы?
for x in ipaddress.ip_network('99.64.0.0/255.192.0.0', False):
    x = f'{x:b}'
    if x[-2:] == '1':
        ct += 1
print(ct)