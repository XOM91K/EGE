import ipaddress
ip = ipaddress.ip_network('210.189.23.15/255.255.248.0', 0)
print(ip[1])