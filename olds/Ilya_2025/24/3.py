import re
s = open(r"C:\Users\Zarif\Downloads\24_624_1 (2).txt").readline()
# Определите максимальную длину последовательности из
# букв {K, N, L, F} в любом порядке,
# которая ограничена по краям одинаковыми чётными цифрами.
m = re.findall(r"0[KNLF]+0|2[KNLF]+2|4[KNLF]+4|6[KNLF]+6|8[KNLF]+8", s)
print(len(max(m, key=len)) - 2)