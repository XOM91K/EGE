import ipaddress
ct = 0
for x in ipaddress.ip_network("99.165.134.0/255.255.254.0", strict=False):
    x = f'{x:b}'
    if x.count('1') % 3 == 0:
        ct += 1
print(ct)