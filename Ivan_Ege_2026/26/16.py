boxes = []
for x in range(230):
    boxes.append([])
a = [[int(d) for d in x.split()] for x in open('16.txt')]
a = sorted(a, key=lambda x: (x[0], x[1]))
c = 0
print(a)
for e in a:
    for box in range(len(boxes)):
        if e[0] not in boxes[box]:
            for i in range(e[0], e[1] + 1):
                boxes[box].append(i)
            c += 1
            print(box + 1)
            break
print(c)
