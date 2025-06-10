import ipaddress
ct = 0
for x in ipaddress.ip_network('202.75.38.160/255.255.255.240', False):
    #x = ''.join([bin(int(d))[2:].zfill(8) for d in str(x).split('.')])
    x = f'{x:b}'
    if '111' in x:
        ct += 1
print(ct)