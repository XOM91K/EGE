import ipaddress
ct = 0
for x in ipaddress.ip_network('186.135.80.0/255.255.252.0', False):
    x = f'{x:b}'
    if x[:16].count('1') > x[-16:].count('1'):
        print(x)
        ct += 1
print(ct)