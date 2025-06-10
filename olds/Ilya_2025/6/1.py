from turtle import *
speed(1000)
# Повтори 7 [Вперёд 10 Направо 120]
color('red', 'blue')
m = 40
left(90)
begin_fill()
for x in range(3):
    forward(10 * m)
    right(120)
end_fill()
ct = 0
for x in range(-500 * m, 500 * m, m):
    for y in range(-500 * m, 500 * m, m):
        f = getcanvas().find_overlapping(x, y, x , y)
        if len(f) > 0 and f[0] == 5:
            print(f)
            ct += 1
print(ct)
done()