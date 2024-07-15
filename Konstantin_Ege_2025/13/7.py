import ipaddress
ct = 0
for x in ipaddress.ip_network('154.24.165.32/255.255.255.224', False):
    x = f'{x:b}'
    if x[:16].count('1') < x[16:].count('1'):
        print(x)
        ct += 1
print(ct)