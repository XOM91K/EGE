import re
s = open(r'C:\Users\Zarif\Downloads\24_31160.txt').readline()
m = re.findall(r'(?=(M{0,3}C{0,3}D?C{0,3}X{0,3}L?X{0,3}I{0,3}V?I{0,3}))', s)
m2 = []
for x in m:
    if x.count('I') <= 3 and x.count('X') <= 3 and x.count('C') <= 3 and x.count('M') <= 3:
        m3 = re.findall(r'I[^I]I|X[^X]X|C[^C]C|M[^M]M|IIV|XXL|CCD', x)
        if len(m3) == 0:
            m2.append(x)
print((max(m2, key=len)))
print(len(max(m2, key=len)))
for x in m2:
    if len(x) == 13 and x.count('M') <= 2:
        print(x)