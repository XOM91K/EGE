elements = input().split()
elements2 = []
print(elements)
for x in elements:
    if elements.count(x) == 1:
        elements2.append(x)
print(elements2)