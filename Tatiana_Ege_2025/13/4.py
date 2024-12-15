#vhttps://examinf.ru/tasks/706
import ipaddress
for net in range(0, 33):
    ip1 = ipaddress.ip_network(f'120.91.176.213/{net}', 0)
    ip2 = ipaddress.ip_network(f'120.91.174.205/{net}', 0)
    if ip1 == ip2:
        print(ip1.netmask, ip2.netmask)