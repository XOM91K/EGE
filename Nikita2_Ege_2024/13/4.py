import ipaddress
d = ipaddress.IPv4Network("135.12.171.214/255.255.248.0", False)
#узнать адрес сети по адресу-узла и маске
print(d)