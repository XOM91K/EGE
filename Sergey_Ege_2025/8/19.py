import itertools
ct = 0
for x in itertools.product("0123456",repeat = 6):
  x = "".join(x)
  ch = x.count("0") + x.count("2")+x.count("4")+x.count("6")
  nech = x.count("1") + x.count("3")+x.count("5")
  if x[0] != "0" and int(x[-1]) >= 4:
    if ch == nech:
      ct += 1
print(ct)