import itertools
#
cnt = 0
for x in itertools.permutations("ЛЕВИЙ", 5):
    x = "".join(x)
    if "ЕИ" not in x and x[0]!="Й":
        cnt+=1
print(cnt)