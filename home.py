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

