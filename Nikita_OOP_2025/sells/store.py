class Store:
    def __init__(self):
        self.products = []
    def __str__(self):
        store_contents = "Ассортимент магазина: \n"
        for product in self.products:
            store_contents += f"{product}\n"
        return store_contents
    def add_product(self, product):
        self.products.append(product) # добавим продукт
        print(f"Товар {product} был добавлен в магазин.")
    def del_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"Товар {product} был убран из магазина.")
        else:
            print(f"Товара {product} нет в магазине.")
    def find_product(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
            print(f"Товар {name} не найден.")
