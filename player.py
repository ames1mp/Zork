from weapon_factory import Weapon
import random


class Player:

    def __init__(self):
        random.seed()
        self.health = random.randrange(100, 126)
        self.attachPower = random.randrange(10, 21)
        self.inventory = [None] * 10
        self.inventory[0] = Weapon.factory("hersheykiss")
        for i in range(1,9):
            random.seed()
            rand = random.randrange(1,4)
            print(repr(rand))
            if rand == 1:
                self.inventory[i] = Weapon.factory("sourstraw")
            if rand == 2:
                self.inventory[i] = Weapon.factory("chocolatebar")
            if rand == 3:
                self.inventory[i] = Weapon.factory("nerdbomb")

    def attack(self, weapon):
        attackData = {"playerBaseAttackPower": self.attachPower,
                      "playerModifiedAttackPower": self.attachPower * weapon.attackMod,
                      "weaponType": weapon.type}
        return attackData

    def defend(self, monsterDamage):
        self.health -= monsterDamage
        if self.health <= 0:
            return "dead"
        return "alive"



