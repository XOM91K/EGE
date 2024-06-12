import ipaddress
ct = 0
for x in ipaddress.ip_network('[вставить свою сетку]/[вставить свою маску]', False):
    x = f'{x:b}' #ЛИБО
    # x = bin(int(x))[2:]
    if x.count('1') % 2 != 0:
        ct += 1
print(ct)