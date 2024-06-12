import ipaddress
ct = 0
for x in ipaddress.ip_network('186.135.80.0/255.255.252.0', False):
    x = f'{x:b}'
    s1 = x[:8]
    s2 = x[8:16]
    s3 = x[16:24]
    s4 = x[24:]
    if s1.count('1') + s2.count('1') > s3.count('1') + s4.count('1'):
        print(x)
        ct += 1
print(ct)