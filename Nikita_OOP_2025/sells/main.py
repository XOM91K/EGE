from Nikita_OOP_2025.sells.product import Product
from Nikita_OOP_2025.sells.shopping_cart import ShoppingCart
from Nikita_OOP_2025.sells.store import Store


def main():
    store = Store()
    t1 = Product("Книга сказки", 750, 3)
    t2 = Product("Книга Триллеры", 1200, 2)
    t3 = Product("Детектив Агата Кристи", 780, 4)
    pen1 = Product("Ручка гелевая красная", 120, 18)
    store.add_product(t1)
    store.add_product(t2)
    store.add_product(t3)
    print(store)
    cart = ShoppingCart()
    cart += t1
    cart += t2
    cart += pen1
    cart += pen1
    cart += pen1
    cart -= pen1
    cart -= pen1
    cart -= pen1
    cart -= pen1
    print(cart.total_price())
    print(cart)


if __name__ == "__main__":
    main()