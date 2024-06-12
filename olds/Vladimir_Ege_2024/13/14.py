import ipaddress
ip = ipaddress.IPv4Network('240.144.182.134/255.255.248.0', strict=False)
print(ip)