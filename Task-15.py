class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def print_info(self):
        print(f'{self.brand} - {self.model}, {self.year}, {self.price}')
