class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 0
        self.happiness = 0

    def display_info(self):
        print(
            f'Name: {self.name} | Age: {self.age} | Health: {self.health} | Happiness: {self.happiness}')

    def feed(self):
        self.health += 10
        self.happiness += 10


class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.health = 50
        self.happiness = 12


class Tiger(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.health = 40
        self.happiness = 7


class Bear(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.health = 60
        self.happiness = 18


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_lion(self, name, age):
        self.animals.append(Lion(name, age))

    def add_tiger(self, name, age):
        self.animals.append(Tiger(name, age))

    def add_bear(self, name, age):
        self.animals.append(Bear(name, age))

    def add_animal(self, animal):
        self.animals.append(animal)

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

    def feed_all_animal(self):
        for animal in self.animals:
            print(
                f' Before feed=> Name: {animal.name}| Health: {animal.health} | Happiness: {animal.happiness}')
            animal.feed()
            print(
                f' After feed=> Name: {animal.name}| Health: {animal.health} | Happiness: {animal.happiness}')
            print("-"*30)


zoo1 = Zoo("Abood Zoo")
zoo1.add_lion("Nala", 5)
zoo1.add_lion("Simba", 7)
zoo1.add_tiger("Rajah", 12)
zoo1.add_tiger("Shere Khan", 13)
zoo1.add_bear("bear", 15)
b1 = Bear("Panda", 13)
zoo1.add_animal(b1)
zoo1.print_all_info()
