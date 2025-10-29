
def s_dec(st1: str, alf2=''):
    alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.'
    a = ''
    for x in range(len(st1)):
        a += alf[alf2.index(st1[x])]
    return a
print(s_dec('CsUU3C0BuLgOZLFt09L2EkJccLctAAaccKtULeG3gAe', 'j0MWqtyn6I5ZDflYP-QX_RsLJuoE49eGHrpSFx2vbdwhzNOVim.7TABK8kcUa31Cg'))
print(s_dec('_W779_B2ZX.uLXkFBdXmb5Y66X6F118663F7Xef9.1e', 'JTR4P-0jEStUDgywiCvHKAoaqrkm1l93Md2n_7xIW5pG6BFZhNbOLQ.8YzfVcesXu'))
# secure_encrypt(input2, local_208,
#                "JTR4P-0jEStUDgywiCvHKAoaqrkm1l93Md2n_7xIW5pG6BFZhNbOLQ.8YzfVcesXu");
# secure_encrypt(local_208, local_308,
#                "j0MWqtyn6I5ZDflYP-QX_RsLJuoE49eGHrpSFx2vbdwhzNOVim.7TABK8kcUa31Cg");