l = [int(x) for x in open('5.txt') if x[0].isdigit()]
print(sum(l) / len(l))