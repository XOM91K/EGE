import ipaddress
ct = 0
for x in ipaddress.ip_network("214.187.224.0/255.255.224.0", False):
    x = bin(int(x))[2:].zfill(32)
    if x.count('1') % 6 != 0 and x[-4:] == '1000':
        ct += 1
        print(ct)