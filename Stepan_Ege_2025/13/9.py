import ipaddress
for mask in range(25, 33):
    ip1 = ipaddress.ip_network(f'121.171.5.70/{mask}', 0)
    ip2 = ipaddress.ip_network(f'121.171.5.107/{mask}', 0)
    if ip1 == ip2:
        print(len(list((ip1))), mask)