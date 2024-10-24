import ipaddress
net = ipaddress.IPv4Network('206.158.124.67/255.255.224.0', False)
print(net)
# 206.158.96.0
k = -1
for x in ipaddress.ip_network('206.158.96.0/255.255.224.0', False):
    x = str(x)
    k += 1
    if x == '206.158.124.67':
        print(k)
