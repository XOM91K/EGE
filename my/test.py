import ipaddress
d = ipaddress.ip_address('213.40.18.72')
g = ipaddress.ip_address('213.40.18.60')
print(f'{d:b}')
print(f'{g:b}')
print(int('11010101', 2)) #213
print(int('00101000', 2)) #40
print(int('00010010', 2)) #18
                        #0
                    #213.40.18.0