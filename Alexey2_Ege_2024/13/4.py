import ipaddress
ct = 0
#2 3 5 7 11 13 17 19 23 29 31
for x in ipaddress.ip_network("172.118.1.255/255.255.252.0", False).hosts():
    x = f'{x:b}'
    if x.count('1') in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
        ct += 1
print(ct)