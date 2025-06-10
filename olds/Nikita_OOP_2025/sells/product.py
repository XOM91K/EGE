
class Product:
    def __init__(self, name, price, stock=0):
        self.name = name
        self.price = price
        self.stock = stock
    def __str__(self):
        return f"{self.name} - {self.price}₽ (В наличии: {self.stock} шт.)"
    def __repr__(self):
        return f"{self.name}"

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.name == self.name and self.price == self.price
        return False

    def __hash__(self):
        return hash(self.__repr__())

# t1 = Product("Книга сказки", 750, 3)
# print(hash(t1))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#