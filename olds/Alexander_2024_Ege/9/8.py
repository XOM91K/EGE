l = [x.split('\t') for x in open(r'C:\Users\Zarif\Downloads\9.txt')]
ct = 0
for x in l:
    if float(x[2].replace(',', '.')) - float(x[1].replace(',', '.')) < -5:
        print(float(x[2].replace(',', '.')), float(x[1].replace(',', '.')))
        if 0 <= int(x[5]) <= 45 or 315 <= int(x[5]) <= 360:
            ct += 1
print(ct)