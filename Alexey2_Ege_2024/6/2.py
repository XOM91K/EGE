from turtle import *
left(90)
speed(1000)
color('blue', 'green')
m = 40
begin_fill()
d = 42
for x in range(2):
    forward(d * m)
    right(90)
    forward(d * m)
    left(90)
right(180)
for x in range(2):
    forward(d * m)
    forward(d * m)
    right(90)
end_fill()
ct = 0
for x in range(-100 * m, 100 * m, m):
    for y in range(-100 * m, 100 * m, m):
        t = getcanvas().find_overlapping(x, y, x, y)
        if len(t) == 1 and t[0] == 5:
            ct += 1
print(ct)
done()