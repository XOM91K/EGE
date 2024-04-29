import ipaddress
for x in range(0, 255):
    y = '51.50.135.169/255.255.255.' + str(x)
    try:
        nt = str(ipaddress.IPv4Network(y, False))[:-3].split('.')
        nt = sum([int(d) for d in nt])
        print(x, nt)
    except:
        None
