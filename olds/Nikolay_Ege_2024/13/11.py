import ipaddress
ip1 = ipaddress.ip_address('211.188.211.49')
ip1 = f'{ip1:b}'
ip2 = ipaddress.ip_address('211.188.200.115')
ip2 = f'{ip2:b}'
print(ip1)
print(ip2)