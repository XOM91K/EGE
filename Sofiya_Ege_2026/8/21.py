import itertools
k=0
for x in itertools.product(sorted('гекэ023'), repeat=4):
    x=''.join(x)
    k+=1
    if x[0]=='2' or x[0]=='0' or x[0]=='3':
        if 'кк' not in x and 'ее' not in x and 'гг' not in x and 'ээ' not in x and '22' not in x and '00' not in x and '33' not in x:
            print(k)
            break