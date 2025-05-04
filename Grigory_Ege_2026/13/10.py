import ipaddress
k = 0
for x in ipaddress.ip_network('192.168.108.157/255.255.255.192',0):
    k += 1
    print(k, x)