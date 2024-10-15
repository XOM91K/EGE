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
        return (self.name, self.x, self.y) == (other.name, other.x, other.y)

    def __lt__(self, other):
        return (self.name, self.x, self.y) < (other.name, other.x, other.y)

    def __gt__(self, other):
        return (self.name, self.x, self.y) > (other.name, other.x, other.y)

    def __le__(self, other):
        return (self.name, self.x, self.y) <= (other.name, other.x, other.y)

    def __ge__(self, other):
        return (self.name, self.x, self.y) >= (other.name, other.x, other.y)

    def __ne__(self, other):
        return (self.name, self.x, self.y) != (other.name, other.x, other.y)


class CheckMark(Point):
    def __init__(self, pt1, pt2, pt3):
        self.pt1 = pt1
        self.pt2 = pt2
        self.pt3 = pt3

    def __str__(self):
        return f'{self.pt1.name}{self.pt2.name}{self.pt3.name}'

    def __repr__(self):
        return f'{self.pt1} {self.pt2} {self.pt3}'

    def __bool__(self):
        string = f'{str(self.pt1)} {str(self.pt2)} {str(self.pt3)}'
        m = re.findall(r'[A-Z]\((-?\d+),(-?\d+)\)', string)
        m = [[int(g) for g in t] for t in m]
        if m[0] == m[1] or m[1] == m[2] or m[0] == m[2]:
            return False
        if (m[0][0] - m[2][0]) * (m[1][1] - m[2][1]) - (m[1][0] - m[2][0]) * (m[0][1] - m[2][1]) == 0:
            return False
        return True


# p_A = Point('A', 1, 2)
# p_B = Point('B', 0, 1)
# p_C = Point('C', -1, 2)
# p_D = Point('D', 2, 2)
# p_E = Point('E', 2, 0)
# p_F = Point('F', 2, -1)
# cm_ABC = CheckMark(p_A, p_B, p_C)
# cm_DEF = CheckMark(p_D, p_E, p_F)
# cm_ABB = CheckMark(p_A, p_B, p_B)
# print(cm_ABC, bool(cm_ABC))
# print(cm_DEF, bool(cm_DEF))
# print(cm_ABB, bool(cm_ABB))

# p_A1 = Point('A', 1, 2)
# p_A2 = Point('A', 2, 1)
# p_B1 = Point('B', 2, 3)
# p_B2 = Point('B', 2, 3)
# print(p_A1 == p_A2, p_B1 == p_B2)
# print(p_A1 != p_A2, p_B1 != p_B2)
# print(p_A1 < p_A2, p_B1 > p_B2)  #
# print(p_A1 >= p_A2, p_B1 <= p_B2)  #
# print(max(p_A1, p_B2, p_A2, p_B2))
# print(min(p_A1, p_B2, p_A2, p_B2))
