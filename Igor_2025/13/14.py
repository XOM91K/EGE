import ipaddress
ct = 0
st = [1, 3, 7, 15, 31, 63, 127, 255]
for x in ipaddress.ip_network('139.75.100.0/255.255.252.0', False):
    #x = bin(int(x))[2:].zfill(32)
    x = str(x).split('.')[-1]
    if int(x) in st:
        ct += 1
print(ct)