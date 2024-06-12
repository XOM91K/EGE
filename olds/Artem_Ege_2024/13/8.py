import ipaddress
ct = 0
for x in ipaddress.ip_network('216.130.64.0/255.255.192.0', False):
    x = str(x).split('.')
    if int(x[0]) % 2 == 0 and int(x[1]) % 2 == 0 and int(x[2]) % 2 == 0 and int(x[3]) % 2 == 0:
        print(x)
        ct += 1
print(ct)