# import ipaddress
# ip1 = ipaddress.ip_address('32.130.201.117')
# print(f'{ip1:b}')
# ip1 = ipaddress.ip_address('255.255.240.0')
# print(f'{ip1:b}')
import ipaddress
ip1 = ipaddress.IPv4Network('32.130.201.117/255.255.240.0', False)
print(ip1)