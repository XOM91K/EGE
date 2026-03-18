import ipaddress

for mask in range(15,33):
    k = 0
    net1 = ipaddress.ip_network(f'143.131.211.37/{mask}', 0)
    for x in net1:
        x = bin(int(x))[2:].zfill(32)
        if x.count('1') == 10:
            k += 1
    if k == 15:
        print(mask)