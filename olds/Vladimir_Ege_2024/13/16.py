import ipaddress
mx = 0
for x in ipaddress.ip_network('204.252.0.0/255.255.0.0', False):
    x = f'{x:b}'
    mx = max(mx, x.count('1'))
print(mx)