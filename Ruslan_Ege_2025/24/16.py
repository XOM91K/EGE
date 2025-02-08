s = open(r'C:\Users\Zarif\Downloads\391_1 (1).txt').readline().split('AXMM')
k = []
for i in s:
    k.append([len(i), i])
print(max(k))
#AXMMASDSSDSDSDASDSADASDASDASDAXMM