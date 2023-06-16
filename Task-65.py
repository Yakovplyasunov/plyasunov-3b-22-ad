class Character:
    def __init__(self, name, level, health, attack, defense):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack
        self.defense = defense

    def apply_damage(self, damage):
        self.health -= damage

    def level_up(self):
        self.level += 1
        self.health *= 1.1
        self.attack *= 1.1


character1 = Character('Персонаж 1', 1, 100, 50, 35)
character2 = Character('Персонаж 2', 1, 100, 60, 25)

for rounds in range(1, 4):
    print(f'Раунд {rounds} ')
    print(f'{character1.name}: Здоровье = {character1.health}, Атака = {character1.attack}')
    print(f'{character2.name}: Здоровье = {character2.health}, Атака = {character2.attack}')

    character2.apply_damage(character1.attack - character2.defense)
    print(f'{character1.name} атакует {character2.name} и наносит урон {character1.attack - character2.defense}')

    character1.apply_damage(character2.attack - character1.defense)
    print(f'{character2.name} атакует {character1.name} и наносит урон {character2.attack - character1.defense}')

    if character1.health <= 0 and character2.health <= 0:
        print('Оба персонажа погибли.')
        break
    elif character1.health <= 0:
        print(f'{character1.name} погиб. {character2.name} победил!')
        break
    elif character2.health <= 0:
        print(f'{character2.name} погиб. {character1.name} победил!')
        break

    character1.level_up()
    character2.level_up()
    print('Персонажи повысили уровни!')
