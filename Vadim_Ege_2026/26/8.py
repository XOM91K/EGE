l = [[int(d) for d in x.split()] for x in open('8.txt')]
customers = [0] * 1440
for x in range(len(customers)):
    for y in l:
        if y[0] <= x <= y[1]:
            customers[x] += 1
print(max(customers))
print(customers)