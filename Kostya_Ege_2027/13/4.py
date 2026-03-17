import ipaddress
ct = 0
for x in ipaddress.ip_network('139.75.100.0/255.255.252.0', 0):
    x = int(str(x).split('.')[-1])
    if x in [31, 63, 127, 255, 15, 7, 3, 1]:
        ct += 1
print(ct)