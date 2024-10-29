import ipaddress
ip = ipaddress.ip_address('121.171.5.70')
ip = f'{ip:b}'
ip1 = ipaddress.ip_address('121.171.5.107')
ip1 = f'{ip1:b}'
print(ip)
print(ip1)