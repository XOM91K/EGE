import ipaddress
ct = 0
#ШИРОКОВЕЩАТЕЛЬНЫЙ - ЭТО ПОСЛЕДНИЙ iP АДРЕС, ОН УСТРОЙСТВАМ НЕ НАЗНАЧАЕТСЯ
for x in ipaddress.ip_network('69.121.128.142/255.255.252.0', 0):
    print(x)