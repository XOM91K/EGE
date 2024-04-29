import ipaddress
ip1 = ipaddress.ip_address('215.171.155.54')
ip1 = f'{ip1:b}'
ip2 = ipaddress.ip_address('215.171.145.37')
ip2 = f'{ip2:b}'
print(ip1)
print(ip2)
print('1' * 20 + '0' * 12)
print(int('11110000', 2))
