import ipaddress
ct = 0
for x in ipaddress.ip_network('158.132.161.128/255.255.255.128', strict=False):
    x = f'{x:b}'
    if x[-1] == '1':
        ct += 1
print(ct)