# kompege № 14360 (Уровень: Сложный)
import ipaddress
for mask in range(17, 33):
    net = ipaddress.ip_network(f'153.202.16.32/{mask}', 0)
    ip = ipaddress.ip_address('153.202.16.37')
    if ip in net:
        print(net.netmask)