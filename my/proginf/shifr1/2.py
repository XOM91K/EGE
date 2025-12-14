import string, itertools
alf = string.ascii_lowercase
bakon = {}
enc = 'BABAB BAABA ABBBA BAABA AABBB BBABA AAAAB AAAAA AAABA ABBBA ABBAB BBBAA AAABA ABAAA ABBBB AABBB AABAA BAAAB BBBAA ABAAA BAABA BBBAA AAAAB AABAA BAABA BAABB BBBAA AABAB ABBBA BAAAB BBBAA BAABA BAABB AAAAA BAAAB BAABB BBBAA AABAB BAAAB BBABB'
enc = enc.split()
ct = 0
for x in itertools.product('AB', repeat=5):
    bakon[''.join(x)] = alf[ct]
    ct += 1
    print(bakon)
    if ct == 26:
        break
bakon['BBBAA'] = '_'
flag = ''
for x in enc:
    if x in bakon:
        flag += bakon[x]
print(flag)