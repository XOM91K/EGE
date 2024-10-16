from itertools import product
ct = 0
for x in product('ТИМОФЕЙ', repeat=6):
    x = ''.join(x)
    x = x.replace("И", "Е")
    x = x.replace("О", "Е")
    if x.count("Е") == 3:
        print(x)
        ct += 1
print(ct)