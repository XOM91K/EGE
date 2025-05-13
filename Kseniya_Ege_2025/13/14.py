import ipaddress
ct = 0
for x in ipaddress.ip_network('139.75.100.0/255.255.252.0', 0):
    x = str(x).split('.')
    if x[-1] in ['1', '3', '7', '15', '31', '63', '127', '255']:
        print(x)
        ct += 1
print(ct)