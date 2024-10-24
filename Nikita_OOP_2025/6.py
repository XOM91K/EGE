import re


class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return self.x, self.y

    def __str__(self):
        return f"{self.name}({self.x},{self.y})"

    def __invert__(self):
        return Point(self.name, self.x, self.y)

    def __repr__(self):
        return f"Point('{self.name}', {self.x},{self.y})"

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

class CheckMark(Point):
    def __init__(self, pt1, pt2, pt3):
        self.pt1 = pt1
        self.pt2 = pt2
        self.pt3 = pt3

    def __str__(self):
        return f'{self.pt1.name}{self.pt2.name}{self.pt3.name}'

    def __repr__(self):
        return f'{self.pt1} {self.pt2} {self.pt3}'

    def __eq__(self, other):
        ops1 = (self.pt1, self.pt2, self.pt3)
        ops2 = (other.pt1, other.pt2, other.pt3)
        ops3 = (self.pt1, self.pt2, self.pt3)
        ops4 = (other.pt3, other.pt2, other.pt1)
        return ops1 == ops2 or ops3 == ops4

    def __bool__(self):
        string = f'{str(self.pt1)} {str(self.pt2)} {str(self.pt3)}'
        m = re.findall(r'\((-?\d+),(-?\d+)\)', string)

        if len(m) < 3:
            return False

        m = [[int(g) for g in t] for t in m]

        if m[0] == m[1] or m[1] == m[2] or m[0] == m[2]:
            return False

        op1 = (m[0][0] - m[2][0]) * (m[1][1] - m[2][1])
        op2 = (m[1][0] - m[2][0]) * (m[0][1] - m[2][1])

        return op1 - op2 != 0