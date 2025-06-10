import itertools
ct = 0
for x in itertools.product("0123456789",repeat=3):
  x = ''.join(x)
  if x[0] != '0' and int(x[0]) <= int(x[1]) <= int(x[2]):
    #print(x)
    ct += 1
print(ct)