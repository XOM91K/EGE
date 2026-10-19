import string
# zwswl{v0x4_f85_r3yv4p_tv0x0g0p_3}
alf = string.ascii_lowercase
flag = 'zwswl{v0x4_f85_r3yv4p_tv0x0g0p_3}'
# vsosh{r0t
#alf = ''.join(sorted('qwertyuiopasdfghjklzxcvbnm'))
print(alf)
for x in range(len(flag)):
    if flag[x].isalpha():
        print(alf[alf.index(flag[x]) - 4], end='')
    else:
        print(flag[x], end='')