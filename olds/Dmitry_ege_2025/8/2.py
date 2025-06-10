import itertools
ct = 0
for x in itertools.product('567', repeat=12):
    x = ''.join(x)
    if '55' not in x:
        ct = ct + 1
print(ct)
# s = 'ПЕТЯ'
# if 'Т' in s:
#     print('Есть')
# s = 'ГОРБУШКА'
# if 'БУШ' in s:
#     print('Есть')
# s = 'ГОРБУШКА'
# if s[3] in 'ОУА':
#     print('Гласная')
# else:
#     print('Согласная')
# s = 'ГОРУБШКА'
# if 'РУБ' not in s:
#     print('Нету')
s = 'abracadabra(*ASDB*(D^@*(V^@D*&d6827dv1td8712d2178d21c5d21782c5s217s65&^SA$S%^$XW^%XS^%@S@$S%^!@S@!B*&S@*S@S@!*&S(!@V^S!@*&S@!S*&@!CS%@!S*C@%S&@S^%@S&*@^!S@%!S&^@!CSC$@!S^&@S$!@X^&SX@$S@^S*&@VS%@B^!N*S(&M)@_!IS@!NSU)(@*B(S@VS^*@SC@%(S&$*@X^SC@%V&S(B*@)NS_*@*SN&*@!^S&(%VC^*@%SX&C@!*VS&(B^*)&N'
print(len(set(s)), len(s)) #возвращает уникальные символы