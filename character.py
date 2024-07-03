# ------------ imports ------------
from weapon import fist, spell_book, duel_axes, sword_and_shield, magic_wand
from health_bar import HealthBar


# class_char: 0 berserker, 1 knight, 2 wizard, 3 priest
import random
class Character:
    def __init__(self,
                 name: str,
                 health: int,
                 class_char: int
                 ) -> None:
        self.name = name
        self.class_char = class_char
        self.health = health
        self.health_max = health

        self.weapon = fist
    def assign_random_weapon(self, weapons: list) -> None:
        random_weapon = random.choice(weapons)
        self.weapon = random_weapon
        print(random_weapon)

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(f"{self.name} dealt {self.weapon.damage} damage to "
              f"{target.name} with {self.weapon.name}")


weapons = [spell_book, duel_axes, magic_wand, sword_and_shield]
class Berserker(Character):
    def __init__(self, name: str="Berserker", health: int = 200) -> None:
        super().__init__(name, health, 0)
        self.health_bar = HealthBar(self, color="red")

class Priest(Character):
    def __init__(self, name: str = "Priest", health: int = 210) -> None:
        super().__init__(name, health, 3)
        self.health_bar = HealthBar(self, color="green")

class Knight(Character):
    def __init__(self, name: str = "knight", health: int = 180) -> None:
        super().__init__(name, health, 1)
        self.health_bar = HealthBar(self, color="white")

class Wizard(Character):
    def __init__(self, name: str = "Wizard", health: int = 170) -> None:
        super().__init__(name, health, 2)
        self.health_bar = HealthBar(self, color="Blue")