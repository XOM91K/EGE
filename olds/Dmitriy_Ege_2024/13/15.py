import ipaddress
ct =0
for A in range(0, 256):
    can = True
    try:
        for x in ipaddress.ip_network(f'246.81.65.{A}/255.255.255.224', strict=False).hosts():
            x = f'{x:b}'
            if (x[16:24].count('0') > x[24:32].count('0')) == 0:
                can = False
                break
    except:
        pass
    if can:
        print(A)
        ct += 1
print(ct)