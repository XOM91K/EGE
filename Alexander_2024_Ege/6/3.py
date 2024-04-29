from turtle import *
color('red', 'blue') #'blue' = 5, 'red' = 4
left(90)
speed(1000)
penup()
m = 10
begin_fill()
for x in range(3):
    right(90)
    forward(369 * m)
    right(90)
    forward(508 * m)
end_fill()
ct = 0
for x in range(-1000 * m, 1000 * m, m):
    for y in range(-1000 * m, 1000 *m, m):
        t = getcanvas().find_overlapping(x, y, x, y)
        if len(t) == 1 and t[0] == 5:
            ct += 1
print(ct)
done()