import ipaddress
ct = 0
for x in ipaddress.ip_network('105.224.200.224/255.255.255.224', False):
    #x = ''.join([bin(int(d))[2:].zfill(8) for d in str(x).split('.')])
    x = f'{x:b}'
    if x.count('1') % 4 == 0:
        print(x)
        ct += 1
print(ct)