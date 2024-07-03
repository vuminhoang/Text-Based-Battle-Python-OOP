# class_weapon: 0 berserker, 1 knight, 2 wizard, 3 priest
class Weapon:
    def __init__(self,
                 name: str,
                 damage: int,
                 class_weapon: int,
                 ) -> None:
        self.name = name
        self.damage = damage
        self.class_weapon = class_weapon





# ------------ object creation ------------
spell_book = Weapon(name="Spell Book",
                    damage=20,
                    class_weapon=3)

duel_axes = Weapon(name="Duel Axes",
                   damage=15,
                   class_weapon=0)

magic_wand = Weapon(name="Magic Wand",
               damage=12,
               class_weapon=2)


sword_and_shield = Weapon(name="Sword and Shield",
               damage=10,
               class_weapon=1)

fist = Weapon(name="Just Fist",
               damage=5,
               class_weapon=None)