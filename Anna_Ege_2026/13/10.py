import ipaddress
ct = 0
n1 = ipaddress.ip_network('192.168.56.192/255.255.255.192')
n2 = ipaddress.ip_network('192.168.56.208/255.255.255.240')
print(len(set(n1).symmetric_difference(set(n2))))
# if n1 != n2:
#     ct += 1
# print(ct)