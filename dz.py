class Product:
    def __init__(self, name, price, in_stock=True):
        self.name = name
        self.price = price
        self.in_stock = in_stock


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        if product.in_stock:
            self.items.append(product)
            print(f"{product.name} додано до кошика.")
        else:
            print(f"{product.name} немає в наявності.")

    def remove_product(self, product):
        if product in self.items:
            self.items.remove(product)
            print(f"{product.name} видалено з кошика.")
        else:
            print(f"{product.name} не знайдено в кошику.")

    def total_price(self):
        total = sum(item.price for item in self.items)
        print(f"Загальна вартість: {total} грн")
        return total

    def show_cart(self):
        print("Ваш кошик:")
        for item in self.items:
            print(f"- {item.name} ({item.price} грн)")
        if not self.items:
            print("Кошик порожній.")

apple = Product("Яблуко", 10)
bread = Product("Хліб", 25)
milk = Product("Молоко", 30, in_stock=False)

my_cart = Cart()

my_cart.add_product(apple)
my_cart.add_product(bread)
my_cart.add_product(milk)

my_cart.show_cart()
my_cart.remove_product(apple)

my_cart.show_cart()
my_cart.total_price()