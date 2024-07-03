# ------------ imports ------------
import os
from character import Berserker, Priest, Wizard, Knight
from weapon import fist, sword_and_shield, spell_book, duel_axes, magic_wand
# ------------ setup ------------

weapons = [spell_book, duel_axes, magic_wand, sword_and_shield]
berserker = Berserker()
berserker.assign_random_weapon(weapons)
priest = Priest()
priest.assign_random_weapon(weapons)

# ------------ game loop ------------
while True:
    os.system("cls")

    berserker.attack(priest)
    priest.attack(berserker)

    berserker.health_bar.draw()
    priest.health_bar.draw()

    if berserker.health <= 0:
        print("Priest wins!")
        break
    elif (priest.health <= 0):
        print("Berserker wins!")
        break

    input()