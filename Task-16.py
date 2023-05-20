class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def print_info(self):
        print(f'кошка по имени {self.name}, возраст {self.age} лет, цвет {self.color}')
