# 20.24.110.42
# 20.24.96.0
import ipaddress
d = ipaddress.ip_address('20.24.110.42')
d = f'{d:b}'
print(d)
d = ipaddress.ip_address('20.24.96.0')
d = f'{d:b}'
print(d)