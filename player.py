########################################################################
# @author Mike Ames
# @author Phil Garza
########################################################################
from weapon_factory import Weapon
import random

########################################################################
# Defines a player.
########################################################################
class Player:

    ########################################################################
    # Constructor. Randomly generates and sets the player's health, attack
    # power, and inventory.
    ########################################################################
    def __init__(self):
        random.seed()
        self.health = random.randrange(100, 126)
        self.attackPower = random.randrange(10, 21)
        self.inventory = []
        self.inventory.append(Weapon.factory("hersheykiss"))
        for i in range(1, 10):
            random.seed()
            rand = random.randrange(1, 4)
            print(repr(rand))
            if rand == 1:
                self.inventory.append(Weapon.factory("sourstraw"))
            if rand == 2:
                self.inventory.append(Weapon.factory("chocolatebar"))
            if rand == 3:
                self.inventory.append(Weapon.factory("nerdbomb"))

    ########################################################################
    # Generates an attack value based on the player's attack power and the
    # weapon the player uses to attack.
    # @return attackData a dictionary which contains the power of the attack
    # as well as the type of weapon used and the player's base attack power
    ########################################################################
    def attack(self, weapon):
        attackData = {"playerBaseAttackPower": self.attackPower,
                      "playerModifiedAttackPower": self.attackPower * weapon.attackMod,
                      "weaponType": weapon.type}
        if weapon.uses != float('inf'):
            weapon.uses -= 1
        if weapon.uses == 0:
            self.inventory.remove(weapon)
        return attackData

    ########################################################################
    # Takes the power of the enemy's attack and adjust the player's health
    # accordingly.
    # @return dead. Whether the player died. Returned to the GUI
    ########################################################################
    def defend(self, monsterDamage):
        self.health -= monsterDamage
        if self.health <= 0:
            return "dead"
        return "alive"



