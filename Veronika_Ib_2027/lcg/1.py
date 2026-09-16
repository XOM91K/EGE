from Crypto.Util.number import long_to_bytes
p = 16616810449074525827
c = 4362608623763405709
c2 = 10489709536418965768
x = 8
flag = (c * pow(x, -1, p)) % p
print(flag)
