class Animal:
    height = 50
    satiety = 100
    age = 10

    def __init__(self):
        print(f"Зріст: {self.height}")
        print(f"Вік: {self.age}")

    def print_info(self):
        print("інформація")


class Dog(Animal):
    height = 60
    age = 5

    def __init__(self):
        super().__init__()
        print("собака")

class Cat(Animal):
    height = 30
    age = 3

    def __init__(self):
        super().__init__()
        print("кіт")

nick = Animal()
nick.print_info()

nick = Cat()
nick.print_info()

nick = Dog()
nick.print_info()
