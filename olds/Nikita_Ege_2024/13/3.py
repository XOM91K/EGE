import ipaddress
#q = ipaddress.IPv4Network('121.171.15.70/121.171.3.68',strict=False)
q = ipaddress.ip_address('121.171.15.70')
q2 = ipaddress.ip_address('121.171.3.68')
print(f'{q:b}')
print(f'{q2:b}')