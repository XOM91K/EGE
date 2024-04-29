import ipaddress
d = ipaddress.IPv4Network("217.8.244.3/255.255.252.0", strict=False)
print(d)