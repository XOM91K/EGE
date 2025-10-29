import itertools
ct=0
for x in itertools.permutations('01234567', 5):
    x=''.join(x)
    if (x[0]=='1')+(x[1]=='2')+(x[2]=='3')+(x[3]=='4')+(x[4]=='5')==2:
        if x.count('1')+x.count('2')+x.count('3')+x.count('4')+x.count('5')>=4:
            ct+=1
print(ct)