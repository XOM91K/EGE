import itertools
ct = 0
for x in itertools.permutations('ГЛУБИНА'):
    x = ''.join(x)
    # x = x.replace("Л", "")
    # x = x.replace("У", "")
    # x = x.replace("Б", "")
    # x = x.replace("Н", "")
    # if ("АИГ" in x) or ("ИАГ" in x):
    if x.index('Г') > x.index('А') and x.index('Г') > x.index('И'):
        ct += 1
print(ct)