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

        # Проверяем, что нашли все три точки
        if len(m) < 3:
            return False

        m = [[int(g) for g in t] for t in m]  # Извлекаем только координаты

        if m[0] == m[1] or m[1] == m[2] or m[0] == m[2]:
            return False

        op1 = (m[0][0] - m[2][0]) * (m[1][1] - m[2][1])
        op2 = (m[1][0] - m[2][0]) * (m[0][1] - m[2][1])

        return op1 - op2 != 0

#
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

# p_A = Point('A', 1, 2)
# p_B = Point('B', 0, 1)
# p_C = Point('C', -1, 2)
# p_D = Point('D', -1, 2)
# cm_ABC = CheckMark(p_A, p_B, p_C)
# cm_CBA = CheckMark(p_C, p_B, p_A)
# cm_ACB = CheckMark(p_A, p_C, p_B)
# cm_ABD = CheckMark(p_A, p_B, p_D)
# cm_DBA = CheckMark(p_D, p_B, p_A)
# print(cm_ABC == cm_CBA, cm_ABC == cm_ABD)
# print(cm_ABC == cm_DBA, cm_ABC == cm_ACB)

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


A1 = Point('P1', -30, 20)
A2 = Point('P2', -10, -10)
A3 = Point('P3', -20, -30)
A4 = Point('P4', 20, -30)
A5 = Point('P5', 30, 20)
A6 = Point('P6', 10, 10)
A7 = Point('P7', 30, 30)

cm_a = CheckMark(A1, A2, A3)
cm_b = CheckMark(A3, A2, A4)
cm_c = CheckMark(A3, A2, A7)
cm_d = CheckMark(A4, A2, A3)
cm_e = CheckMark(A2, A6, A7)
cm_f = CheckMark(A7, A5, A6)
cm_g = CheckMark(A1, A1, A6)
cm_h = CheckMark(A4, A5, A4)
cm_i = CheckMark(A3, A3, A3)

print(bool(cm_a))
print(bool(cm_b))
print(bool(cm_c))
print(bool(cm_d))
print(bool(cm_e))
print(bool(cm_f))
print(bool(cm_g))
print(bool(cm_h))
print(bool(cm_i))