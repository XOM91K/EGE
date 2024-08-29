s = input()
symbol = ord(s[0])
number = int(s[-1])
if symbol % 2 == 0 and number % 2 == 0:
    print('BLACK')
elif symbol % 2 == 1 and number % 2 == 1:
    print('BLACK')
else:
    print('WHITE')