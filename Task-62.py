class Robot:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def movement(self, time):
        print(f'Робот {self.name} прошел за время {time} расстояние - {time * self.speed}')


class CaterpillarRobot(Robot):
    def __init__(self, name, speed, territory):
        super().__init__(name, speed)
        self.territory = territory


class WheeledRobot(Robot):
    def __init(self, name, speed, brand):
        super().__init__(name, speed)
        self.brand = brand
