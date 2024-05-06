import ipaddress
for a in range(256):
    try:
        can = True
        for x in ipaddress.ip_network(f'252.63.194.3/255.255.{a}.0',False):
            x=bin(int(x))[2:]
            if x[:16].count('1') < x[16:].count('1'):
                can = False
        if can:
            print(a)
    except:
        pass