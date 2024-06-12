import ipaddress
#ip_network - создаёт сеть и возвращает айпи адреса
#нужна "сеть" и "маска"
#IPv4Network - возвращает адрес сети из айпи адреса узла и маски
#ip_address - переводит строку в формат айпиадреса
ct = 0
for x in ipaddress.ip_network('213.0.0.0/255.192.0.0', False):
    x = f'{x:b}'
    if '111' in x:
        ct +=1
print(ct)