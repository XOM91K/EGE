from turtle import *
m = 30
speed(1000)
left(90)
color('violet', 'red')
begin_fill()
for x in range(3):
    forward(10 * m)
    right(120)
end_fill()
ct = 0
for x in range(-100 * m, 100 * m, m):
    for y in range(-100 * m, 100 * m, m):
        t = getcanvas().find_overlapping(x, y, x, y)
        if len(t) > 0 and t[0] == 5:
            ct += 1
print(ct)
done()