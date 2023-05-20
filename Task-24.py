class Worker:
    def __init__(self, name, age, salery):
        self.name = name
        self.age = age
        self.salery = salery

    def give_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Зарплата: {self.salery}")

worker_obj = Worker("Вася", 46, 150000)

worker_obj.give_info()
