from Nikita_OOP_2025.sells.product import Product


class ShoppingCart:
    def __init__(self):
        self.items = {}
    def __str__(self):
        if not self.items:
            return 'Корзина пуста.'
        cart_contents = "Корзина:\n"
        for product, q in self.items.items():
            cart_contents += f"{product.name} x {q} - ₽{product.price * q}\n"
        cart_contents += f"Общая стоимость: ₽{self.total_price()}"
        return cart_contents
    def __repr__(self):
        return f"ShoppingCart({self.items})"

    def __add__(self, product):
        if product in self.items:
            self.items[product] += 1
            product.stock -= 1
        else:
            if product.stock > 0:
                self.items[product] = 1
                product.stock -= 1
            else:
                print(f"Товара '{product.name}' больше нет в наличии!")
        return self
    def __sub__(self, product):
        if product in self.items:
            self.items[product] -= 1
            product.stock += 1
        if product not in self.items:
            raise IndexError(f"Товара {product.name} нет корзине")
        if self.items[product] == 0:
            del self.items[product]
        else:
            print(f"Товар '{product.name}' был удалён из корзины.")
        return self
    def __len__(self):
        return len(self.items)
    def __getitem__(self, index):
        if index < 0 or index >= len(self.items):
            raise IndexError("Индекс не найден!")
        product = list(self.items.keys())[index]
        return (product, self.items[product])
    def total_price(self):
        return sum(product.price * q for product, q in self.items.items())
# t1 = Product("Книга сказки", 750, 3)
# shopc = ShoppingCart()
# shopc += t1
# shopc += t1
# shopc -= t1
# print(shopc)

