import ipaddress
ct = 0
for x in ipaddress.ip_network('95.112.224.0/255.255.255.128', False):
    d = bin(int(x))[2:]
    g = f'{x:b}'
    r = ''.join([bin(int(t))[2:].zfill(8) for t in str(x).split('.')])
    if str(x).split('.')[-1] == str(x).split('.')[-1][::-1]:
        ct += 1
print(ct)