import ipaddress
for x in ipaddress.ip_network('192.168.248.176/255.255.255.240', False):
    x = str(x).split('.')
    x = ''.join([bin(int(d))[2:].zfill(8) for d in x])
    if x.count('1') > x.count('0'):
        print(x)