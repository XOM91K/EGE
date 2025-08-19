labubu = [[int(cheburashka) for cheburashka in xolop.split()] for xolop in open('777.txt')]
pikmei = 0
for x in labubu:
    if len(set(x)) == 5:
        xolop=sorted(x)
        otr = [y for y in x if y < 0]
        pol = [y for y in x if y > 0]
        if abs(sum(otr)) > sum(pol):
            pikmei += 1
print(pikmei)
