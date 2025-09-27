import ipaddress
ct = 0
for x in ipaddress.ip_network('139.75.100.0/255.255.252.0'):
    x = str(x).split('.')
    for n in range(1, 9):
        if 2 ** n - 1 == int(x[-1]):
            ct += 1
print(ct)