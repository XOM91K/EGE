import ipaddress
ct = 0
for x in ipaddress.ip_network("184.178.54.144/255.255.255.240", strict=False):
    x = f'{x:b}'
    if '111' in x:
        #print(x)
        ct += 1
print(ct)