l = open(r'C:\Users\Zarif\Downloads\1754_1 (1).txt').readline()
l = l.split('.')
print(l)
c = []
for x in l:
    if x.count('M') > 50:
        print(x)
        c.append(len(x)+1)
print(max(c))
#Нет предложений, в которых ровно 112 М