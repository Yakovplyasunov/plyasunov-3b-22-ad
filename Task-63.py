class ProductCard:
    def __init__(self, name, cost, quantity):
        self.name = name
        self.cost = cost
        self.quantity = quantity

    def decrease_quantity(self, number):
        if self.quantity - number >= 0:
            self.quantity -= number
            print(f'Количество уменьшено на {number}. Теперь количество равно {self.quantity}')
        else:
            print(f'Нельзя уменьшить количество на {number}')

    def changing_cost(self, number):
        if self.cost + number >= 0:
            self.cost += number
            print(f'Стоимость изменена на {number}. Стоимость равна {self.cost}')
        else:
            print(f'Нельзя изменить стоимость на {self.cost}')
