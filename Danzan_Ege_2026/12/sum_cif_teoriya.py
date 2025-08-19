s = '31231231231273210931273129037123012371'
#print(sum(list(s)))
print(sum([int(x) for x in s]))
print(sum(map(int, s))) # summapint