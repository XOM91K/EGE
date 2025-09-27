import ipaddress
ct=0
for x in ipaddress.ip_network('90.65.32.0/255.255.224.0',0):
    x = bin(int(x))[2:].zfill(32)
    if x.count('0')==x.count('1'):
        ct+=1
print(ct)