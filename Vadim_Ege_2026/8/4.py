from itertools import*
x = product("БНПЭ", repeat =4)
i = 0
#s =list()
for k in x:
    k = ''.join(k)
    i+=1
    if i % 2 == 0 and k[0] != "П" and k[-1] != "П" and 'ЭЭ' not in k:
        print(i,k)