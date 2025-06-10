import ipaddress

net = ipaddress.
('11.92.135.56/255.224.0.0', strict=False)
for ip in net:
    print(str(ip))
    print(bin(int(ip))[2:].zfill(32))