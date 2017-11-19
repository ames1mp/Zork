import random
from observer import Observer
from observable import Observable
from mob_factory import Mob, MonsterTypes


class Home(Observable, Observer):
    def __init__(self):
        super().__init__()
        random.seed()
        numMonsters = random.randrange(1, 11)

        self.monsters = []

        for i in range(numMonsters):
            # represents the type of monster to be created
            monsterRand = random.randrange(1, 5)

            # get the name of the monster defined in the enum in the mob_factory module and use it
            # to create a new monster and add it to the home's list
            monster = Mob.factory(MonsterTypes(monsterRand).name)
            self.monsters.append(monster)
            monster.addObserver(self)

        self.numBaddies = len(self.monsters)

    def update(self, other):
        self.monsters.remove(other)
        self.numBaddies -= 1
        self.monsters.append(Mob.factory("person"))
        super().update(self)



# class Driver:
#
#     if __name__ == '__main__':
#
#         attackData = {"playerBaseAttackPower": 10,
#                       "playerModifiedAttackPower": 25,
#                       "weaponType": "hersheykiss"}
#
#         home = Home()
#         print("Num Monsters: " + repr(len(home.monsters)))
#         print("Monster 0  is " + home.monsters[0].type)
#         print("Monster 0 has HP: " + repr(home.monsters[0].health))
#         home.monsters[0].defend(attackData)
#         print("Num Monsters: " + repr(len(home.monsters)))
#         print("Monster 0 has HP: " + repr(home.monsters[0].health))
#         home.monsters[0].defend(attackData)
#         print("Num Monsters: " + repr(len(home.monsters)))
#         print("Monster 0 has HP: " + repr(home.monsters[0].health))
#         home.monsters[0].defend(attackData)
#         print("Num Monsters: " + repr(len(home.monsters)))
#         print("Monster 0 has HP: " + repr(home.monsters[0].health))
#         home.monsters[0].defend(attackData)
#         print("Num Monsters: " + repr(len(home.monsters)))
#         print("Monster 0 has HP: " + repr(home.monsters[0].health))
#         home.monsters[0].defend(attackData)
#         print("Num Monsters: " + repr(len(home.monsters)))
#         print("Monster 0 has HP: " + repr(home.monsters[0].health))
#         home.monsters[0].defend(attackData)
#         print("Num Monsters: " + repr(len(home.monsters)))
#         print("Monster 0 has HP: " + repr(home.monsters[0].health))

