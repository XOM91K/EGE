import ipaddress
mx_sm = []
for x in ipaddress.ip_network('134.80.0.0/255.240.0.0', 0):
    d = x
    x = bin(int(x))[2:].zfill(32)
    if x.count('0') == x.count('1'):
        sm = [int(d) for d in str(d).split('.')]
        mx_sm.append(sum(sm))
print(max(mx_sm))