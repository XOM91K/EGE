import ipaddress
ct = 0
for x in ipaddress.ip_network('105.224.200.224/255.255.255.224', False):
    x = str(x).split('.')
    for i in range(len(x)):
        x[i] = bin(int(x[i]))[2:].zfill(8)
    x = ''.join(x)
    if x.count('1') % 4 == 0:
        ct += 1
        print(x)
print(ct)