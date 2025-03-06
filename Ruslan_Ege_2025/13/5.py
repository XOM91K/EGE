from ipaddress import*

for mask in range(10, 32):
    n1 = ip_network(f'211.188.211.49/{mask}', 0)
    n2 = ip_network(f'211.188.200.115/{mask}', 0)
    if n1 == n2:
        k = 0
        for ip in n1:
            ip = bin(int(ip))[2:].zfill(32)
            if ip.count('1') % 2 != 0:
                k+=1
        print(k)