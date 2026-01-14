# По заданным IP-⁠адресу узла и маске определите адрес сети.
# IP адрес узла: 217.9.142.131
# Маска: 255.255.192.0
import ipaddress
net=ipaddress.ip_network(f'217.9.142.131/255.255.192.0', 0)
for ip in net:
    print(ip)