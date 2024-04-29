import ipaddress
for A in range(0, 256):
    for x in ipaddress.ip_network(f'227.31.{A}.139/255.255.255.224', False):
        x = f'{x:b}'
        if x[:16].count('0') > x[-16:].count('0'):
            break
    else:
        print(A)