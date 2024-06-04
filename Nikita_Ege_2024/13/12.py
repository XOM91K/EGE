import ipaddress
ct = 0
for x in ipaddress.ip_network('122.159.136.144/255.255.255.248', False):
    d = f'{x:b}' #1-й способ
    g = bin(int(x))[2:] #2-й способ
    t = ''.join([bin(int(t))[2:].zfill(8) for t in str(x).split('.')]) #3-й способ
    if t.count('1') % 4 != 0:
        ct += 1
print(ct)