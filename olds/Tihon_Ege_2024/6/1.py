from turtle import *
m = 20
color('red', 'blue')
speed(1000)
left(90)
right(90)
begin_fill()

for x in range(3):
    right(45)
    forward(10 * m)
    right(45)
right(315)
forward(10 * m)
for x in range(2):
    right(90)
    forward(10 * m)
end_fill()
ct = 0
for x in range(-100 * m, 100 * m, m):
    for y in range(-100 * m, 100 * m, m):
        t = getcanvas().find_overlapping(x, y, x, y)
        if len(t) == 1 and t[0] == 5:
            print(t)
            ct += 1
print(ct)
done()
