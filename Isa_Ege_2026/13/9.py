import ipaddress
ct = 0
for x in ipaddress.ip_network('111.194.0.0/255.254.0.0'):
    a = bin(int(x))[2:].zfill(32)
    print(a)
    if (a.count('1') - a.count('0'))%2 == 0 :
        ct += 1
print(ct)