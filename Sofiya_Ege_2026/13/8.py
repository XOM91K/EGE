import ipaddress
for x in range(0, 32):
    s = '1' * x + '0' + '1' * (31-x)
    print(s)