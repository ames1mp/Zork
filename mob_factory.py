########################################################################
# @author Mike Ames
# @author Phil Garza
########################################################################

import random
from observable import Observable
from enum import Enum
# Factory code adapted from:
# http://python-3-patterns-idioms-test.readthedocs.io
# /en/latest/Factory.html

########################################################################
# An enum class which defines the types of monsters.
########################################################################
class MonsterTypes(Enum):
    person = 0
    zombie = 1
    vampire = 2
    ghoul = 3
    werewolf = 4

########################################################################
# This is a factory class which generates monsters according to the
# type passed in. It also defines the actions a monster may perform.
########################################################################
class Mob(Observable):

    ####################################################################
    # Factory method. Generates a monster of the appropriate type
    # @ return A monster object.
    ####################################################################
    def factory(type):
        if type == "person": return Person()
        if type == "zombie": return Zombie()
        if type == "vampire": return Vampire()
        if type == "ghoul": return Ghoul()
        if type == "werewolf": return Werewolf()
        assert 0, "Invalid type: " + type
    factory = staticmethod(factory)

    ####################################################################
    # Attack method. Returns the monster's attack power.
    # @ return attackPower the monster's attack power.
    ####################################################################
    def attack(self):
        return self.attackPower

    ####################################################################
    # Defend method. Takes an attack dictionary from the player.
    # Computes the damage dealt to the monster, taking into account
    # the monster's resistances and weaknesses, and adjust's the
    # monster's health accordingly. If the monster dies it notifies the
    # house in which it resides.
    # @ return damage The damage done to the monster. Returned to the
    # GUI
    # @Return dead Whether the monster died. Returned to the GUI
    ####################################################################
    def defend(self, attackData):
        dead = False
        if self.type == "person":
            damage = 0
        elif attackData["weaponType"] == self.immunity[0]:
            damage = 0
        elif len(self.immunity) == 2 and attackData["weaponType"] == self.immunity[1]:
            damage = 0
        elif attackData["weaponType"] == self.weakness:
            if self.type == "zombie":
                damage = 2 * attackData["playerModifiedAttackPower"]
            if self.type == "zombie":
                damage = 5 * attackData["playerModifiedAttackPower"]
        else:
            damage = attackData["playerModifiedAttackPower"]

        self.health = self.health - damage

        if self.health <= 0:
            super().update(self)
            dead = True
        return {"damage": damage, "dead": dead}

####################################################################
# Child Classes of Mob. They set the fields for each monster type
####################################################################
class Person(Mob):
    def __init__(self):
        super().__init__()
        self.type = "person"
        self.health = 100
        self.attackPower = -10
        self.weakness = "none"
        self.immunity = ["none"]


class Zombie(Mob):
    def __init__(self):
        super().__init__()
        self.type = "zombie"
        random.seed()
        self.health = random.randrange(50,101)
        self.attackPower = random.randrange(0,11)
        self.weakness = "SourStraw"
        self.immunity = ["none"]


class Vampire(Mob):
    def __init__(self):
        super().__init__()
        self.type = "vampire"
        random.seed()
        self.health = random.randrange(100,201)
        self.attackPower = random.randrange(10,16)
        self.weakness = "none"
        self.immunity = ["ChocolateBar"]


class Ghoul(Mob):
    def __init__(self):
        super().__init__()
        self.type = "ghoul"
        random.seed()
        self.health = random.randrange(40,81)
        self.attackPower = random.randrange(15,22)
        self.weakness = "NerdBombs"
        self.immunity = ["none"]


class Werewolf(Mob):
    def __init__(self):
        super().__init__()
        self.type = "werewolf"
        random.seed()
        self.health = 200
        self.attackPower = random.randrange(0, 41)
        self.weakness = "none"
        self.immunity = ["ChocolateBar", "SourStraw"]