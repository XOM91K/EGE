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
        return f"{self.name}({self.x}, {self.y})"

    def __invert__(self):
        return Point(self.name, self.y, self.x)

    def __repr__(self):
        return f"Point('{self.name}', {self.x}, {self.y})"

    def __eq__(self, other): # ==
        return (self.name, self.y, self.x) == (other.name, other.y, other.x)

    def __lt__(self, other): # <
        return (self.name, self.y, self.x) < (other.name, other.y, other.x)

p_A1 = Point('A', 1, 1)
p_A2 = Point('A', 1, 1)
p_B1 = Point('B', 2, 3)
p_B2 = Point('B', 2, 3)
print(p_A1 == p_A2)
