import random
from enum import Enum
# Factory code adapted from: http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html


class MonsterTypes(Enum):
    person = 1
    zombie = 2
    vampire = 3
    ghoul = 4
    werewolf = 5


class Mob(object):

    def factory(type):
        if type == "person": return Person()
        if type == "zombie": return Zombie()
        if type == "vampire": return Vampire()
        if type == "ghoul": return Ghoul()
        if type == "werewolf": return Werewolf()
        assert 0, "Invalid type: " + type
    factory = staticmethod(factory)

    def attack(self):
        return self.attackPower

    def defend(self, attackData):
        if attackData["weaponType"] == self.immunity[0]:
            return
        if len(self.immunity) == 2 and attackData["weaponType"] == self.immunity[1]:
            return
        if attackData["weaponType"] == self.weakness:
            if self.type == "zombie":
                damage = 2 * attackData["playerModifiedAttackPower"]
            if self.type == "zombie":
                damage = 5 * attackData["playerModifiedAttackPower"]
        else:
            damage = attackData["playerModifiedAttackPower"]

        self.health = self.health - damage

        if self.health <= 0:
            return "dead"
        return "alive"


class Person(Mob):
    def __init__(self):
        self.type = "person"
        self.health = 100
        self.attackPower = -1
        self.weakness = "none"
        self.immunity = ["none"]


class Zombie(Mob):
    def __init__(self):
        self.type = "zombie"
        random.seed()
        self.health = random.randrange(50,101)
        self.attackPower = random.randrange(0,11)
        self.weakness = "SourStraw"
        self.immunity = ["none"]


class Vampire(Mob):
    def __init__(self):
        self.type = "Vampire"
        random.seed()
        self.health = random.randrange(100,201)
        self.attackPower = random.randrange(10,21)
        self.weakness = "none"
        self.immunity = ["ChocolateBar"]


class Ghoul(Mob):
    def __init__(self):
        self.type = "ghoul"
        random.seed()
        self.health = random.randrange(40,81)
        self.attackPower = random.randrange(15,31)
        self.weakness = "NerdBombs"
        self.immunity = ["none"]


class Werewolf(Mob):
    def __init__(self):
        self.type = "werewolf"
        random.seed()
        self.health = 200
        self.attackPower = random.randrange(0,41)
        self.weakness = "none"
        self.immunity = ["ChocolateBar", "SourStraw"]