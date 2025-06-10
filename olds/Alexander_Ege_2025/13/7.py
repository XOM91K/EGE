import ipaddress
ct = 0
for x in ipaddress.ip_network('139.75.100.0/255.255.252.0', 0):
    x = str(x)
    x = x.split('.')
    if int(x[-1]) == 1 or int(x[-1]) == 3 or int(x[-1]) == 7 or int(x[-1]) == 15 or int(x[-1]) == 31 or int(x[-1]) == 63 or int(x[-1]) == 127 or int(x[-1]) == 255:
        ct += 1
print(ct)