import ipaddress
d = ipaddress.IPv4Network('146.212.200.55/255.255.240.0', strict=False)
print(d.network_address)