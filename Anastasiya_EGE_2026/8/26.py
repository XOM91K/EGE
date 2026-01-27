import string
print(string.ascii_letters)
import itertools
ct=0
for x in itertools.product('0123456789ABCDEFGHIJKLMNO',repeat=4):
    x=''.join(x)
    sm_cif = 0
    for y in x:
        sm_cif += int(y, 25)
    if x[0]!='0' and sm_cif % 5 == 0:
        x = x.replace('0', '*')
        x = x.replace('2', '*')
        x = x.replace('4', '*')
        x = x.replace('6', '*')
        x = x.replace('8', '*')
        x = x.replace('A', '*')
        x = x.replace('C', '*')
        x = x.replace('E', '*')
        x = x.replace('G', '*')
        x = x.replace('I', '*')
        x = x.replace('K', '*')
        x = x.replace('M', '*')
        x = x.replace('O', '*')
        x = x.replace('1', '#')
        x = x.replace('3', '#')
        x = x.replace('5', '#')
        x = x.replace('7', '#')
        x = x.replace('9', '#')
        x = x.replace('B', '#')
        x = x.replace('D', '#')
        x = x.replace('F', '#')
        x = x.replace('H', '#')
        x = x.replace('J', '#')
        x = x.replace('L', '#')
        x = x.replace('N', '#')
        if '##' not in x and '**' not in x:
            ct+=1
print(ct)