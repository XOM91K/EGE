import ipaddress
ct = 0
for x in ipaddress.ip_network('99.64.0.0/255.192.0.0', False):
    x = str(x).split('.')
    if bin(int(x[-1]))[-2:] == '11':
        ct += 1
print(ct)