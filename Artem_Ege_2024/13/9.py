import ipaddress
ct = 0
for x in ipaddress.ip_network('140.19.96.0/255.255.248.0', False):
    x = f'{x:b}'
    s1 = x[:8]
    s2 = x[8:16]
    s3 = x[16:24]
    s4 = x[24:]
    if s1.count('1') == s2.count('1') == s3.count('1') == s4.count('1'):
        ct += 1
print(ct)