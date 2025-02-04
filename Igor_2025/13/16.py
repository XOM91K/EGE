import ipaddress
mn = []
for mask in range(16, 33):
    ip1_network = ipaddress.ip_network(f'157.220.185.237/{mask}', 0)
    ip2_network = ipaddress.ip_network(f'157.220.184.230/{mask}', 0)
    if ip1_network == ip2_network:
        cnt = 0
        print(mask, len(list(ip2_network)))
        for x in ip2_network:
            if bin(int(x))[2:].zfill(32).count('1') == 15:
                cnt += 1
        mn.append(cnt)
        print(mask, cnt)
print(min(mn))