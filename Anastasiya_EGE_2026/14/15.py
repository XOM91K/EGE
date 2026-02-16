import string
print(string.ascii_uppercase)
for x in '0123456789ABCDEFGHIJKLMNOPQRSTUVW':
    c1 = int(f'gp45{x}2', 34)
    c2 = int(f'p7{x}', 34)
    c3 = int(f'{x}ai98', 34)
# for x in range(0,1000):
#     c1=16*34**5 + 25*34**4 + 4*34**3 + 5*34**2 + x*34 + 2
#     c2=25*34**2 + 7*34 + x
#     c3=x*34**4 + 10*34**3 + 18*34**2 + 9*34 + 8

    if (c1+c2*c3)%13==0:
        print((c1+c2*c3)//13)