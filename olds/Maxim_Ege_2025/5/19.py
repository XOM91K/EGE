alf = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'a', 'b', 'c', 'd', 'e', 'f']
print(alf)
for N in range(3,1000):
    R = hex(N)[2:]
    sm_cif = 0
    for x in R:
        sm_cif += alf.index(x)
    if sm_cif %2==0:
        R += 'F'
    else:
        R += '1'
    R = int(R, 16)
    if R <= 300:
        print(N)