import random

## Factory code adapted from: http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html
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

    def defend(self, playerAttack, playerWeapon):
        if playerWeapon == self.immunity[0]:
            return
        if len(self.immunity) == 2 and playerWeapon == self.immunity[1]:
            return
        if playerWeapon == self.weakness:
            if self.type == "zombie":
                damage = 2 * playerAttack
            if self.type == "zombie":
                damage = 5 * playerAttack
        else:
            damage = playerAttack

        self.health = self.health - damage



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
        self.health = random.randrange(50,100)
        self.attackPower = random.randrange(0,10)
        self.weakness = "SourStraw"
        self.immunity = ["none"]

class Vampire(Mob):
    def __init__(self):
        self.type = "Vampire"
        random.seed()
        self.health = random.randrange(100,200)
        self.attackPower = random.randrange(10,20)
        self.weakness = "none"
        self.immunity = ["ChocolateBar"]

class Ghoul(Mob):
    def __init__(self):
        self.type = "ghoul"
        random.seed()
        self.health = random.randrange(40,80)
        self.attackPower = random.randrange(15,30)
        self.weakness = "NerdBombs"
        self.immunity = ["none"]

class Werewolf(Mob):
    def __init__(self):
        self.type = "werewolf"
        random.seed()
        self.health = 200
        self.attackPower = random.randrange(0,40)
        self.weakness = "none"
        self.immunity = ["ChocolateBar", "SourStraw"]

class Driver:

    if __name__ == '__main__':

        zomb = Mob.factory("zombie")
        print("Zombie's Health is " + repr(zomb.health))
        zomb.defend(10, "SourStraw")
        print("Zombie's Health is " + repr(zomb.health))


