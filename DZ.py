class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, species="Собака")

    def speak(self):
        return "Гав-гав!"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, species="Кіт")

    def speak(self):
        return "Мяу!"
