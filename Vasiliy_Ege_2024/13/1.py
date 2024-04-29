import ipaddress
ip = ipaddress.IPv4Network("32.130.201.117/255.255.240.0", strict=False)
print(ip)