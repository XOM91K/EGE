import ipaddress
ct=0
for x in ipaddress.ip_network('23.140.159.160/255.255.252.0',False):
    x=f'{x:b}'
    if x[16:].count('1')>=x[-16:].count('1'):
        ct+=1
print(ct)