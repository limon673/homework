import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.energy = 50
        self.alive = True

    def to_eat(self):
        self.energy += 10
        self.gladness += 3
        print("Yummy! The cat is eating.")

    def to_sleep(self):
        self.energy += 5
        self.gladness += 2
        print("The cat is sleeping peacefully.")

    def to_play(self):
        self.gladness += 7
        self.energy -= 8
        print("The cat is playing with a toy.")

    def to_ignore(self):
        self.gladness -= 6
        print("The cat is being ignored...")

    def is_alive(self):
        if self.gladness < 0:
            print("The cat is too sad and runs away...")
            self.alive = False
        elif self.energy < 0:
            print("The cat is exhausted and collapses...")
            self.alive = False
        elif self.gladness > 100:
            print("The cat is living its best life and goes exploring!")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness: {self.gladness}")
        print(f"Energy: {self.energy}")

    def live(self, day):
        day_str = f"Day {day} of {self.name}'s life"
        print(f"{day_str:=^50}")
        activity = random.randint(1, 4)
        if activity == 1:
            self.to_eat()
        elif activity == 2:
            self.to_sleep()
        elif activity == 3:
            self.to_play()
        elif activity == 4:
            self.to_ignore()
        self.end_of_day()
        self.is_alive()


mia = Cat(name="mia")

for day in range(1, 366):
    if not mia.alive:
        break
    mia.live(day)
