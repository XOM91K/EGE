from turtle import *
color('red', 'blue') #'blue' = 5, 'red' = 4
left(90)
speed(1000)
m = 40
begin_fill()
for x in range(3):
    forward(10 * m)
    right(120)
end_fill()
ct=  0
for x in range(-100 * m, 100 * m, m):
    for y in range(-100 * m, 100 *m, m):
        t = getcanvas().find_overlapping(x, y, x, y)
        if len(t) == 1 and t[0] == 5:
            ct += 1
print(ct)
done()