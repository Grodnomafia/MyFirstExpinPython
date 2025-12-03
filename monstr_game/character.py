class Character:
    def __init__(self,name,health,damage):
        self.name = name
        self.health = health
        self.max_health = health
        self.damage = damage
        self.alive = True


    def attack(self,target):
        if target.alive:
            target.health -= self.damage
            print(f'{self.name} атакует {target.name}! Наносит {self.damage} Осталась хп {target.health}')
            if target.health <= 0:
                target.health = 0
                target.alive = False
                print(f"⚰️ {target.name} погиб!")
    def take_damage(self, amount):
        """Получить урон"""
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.alive = False
            print(f"{self.name} погиб!")

    def is_alive(self):
        """Проверить, жив ли персонаж"""
        return self.health > 0