import ipaddress
for x in ipaddress.ip_network('20.24.110.42/20.24.96.0'):
    print(x)