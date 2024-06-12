import ipaddress


def get_prime(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True
ct = 0
for x in ipaddress.ip_network("172.118.1.255/255.255.252.0", False).hosts():
    x = f'{x:b}'
    if get_prime(x.count('1')):
        ct += 1
print(ct)