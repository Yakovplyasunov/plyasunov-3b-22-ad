class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def print_info(self):
        print(f'Имя собаки: {self.name}')
        print(f'Порода собаки: {self.breed}')
        print(f'Возраст собаки: {self.age}')
