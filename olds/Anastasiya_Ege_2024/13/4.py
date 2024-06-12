import ipaddress
for A in range(0, 256):
    can = True
    for x in ipaddress.ip_network(f'154.127.{A}.230/255.255.255.192', False):
        x = f'{x:b}'
        if x[:16].count('1') <= x[-16:].count('1'):
            can = False
    if can:
        print(A)