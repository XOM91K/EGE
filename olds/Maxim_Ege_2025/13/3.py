import ipaddress
ct = 0
for x in ipaddress.ip_network('186.135.80.0/255.255.252.0',False):
    x = str(x)
    x = x.split('.')
    x[0] = bin(int(x[0]))[2:].zfill(8)
    x[1] = bin(int(x[1]))[2:].zfill(8)
    x[2] = bin(int(x[2]))[2:].zfill(8)
    x[3] = bin(int(x[3]))[2:].zfill(8)
    if (x[0].count('1') + x[1].count('1')) > (x[2].count('1') + x[3].count('1')):
            ct += 1
            print(ct, x)