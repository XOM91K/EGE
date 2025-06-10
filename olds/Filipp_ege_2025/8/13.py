from itertools import product
ct = 0
letters = 'СВЯТОСЛАВ'
for x in set(product(letters, repeat=7)):
    x = ''.join(x)
    x = x.replace("С", "1")
    x = x.replace("В", "1")
    x = x.replace("Я", "0")
    x = x.replace("Т", "1")
    x = x.replace("О", "0")
    x = x.replace("С", "1")
    x = x.replace("Л", "1")
    x = x.replace("А", "0")
    if x.count("1") < x.count("0"):
        ct += 1

print(ct)