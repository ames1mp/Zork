import random
from mob_factory import Mob, MonsterTypes


class Home:
    def __init__(self):
        random.seed()
        numMonsters = random.randrange(1, 11)

        self.monsters = []

        for i in range(numMonsters):
            # represents the type of monster to be created
            monsterRand = random.randrange(1, 6)

            # get the name of the monster defined in the enum in the mob_factory module and use it
            # to create a new monster and add it to the home's list
            self.monsters.append(Mob.factory(MonsterTypes(monsterRand).name))


class Driver:

    if __name__ == '__main__':

        home = Home()
        print("Num Monsters: " + repr(len(home.monsters)))
        print("Monster 0  is " + home.monsters[0].type)
        print("Monster 1  is " + home.monsters[1].type)
        print("Monster 0 has HP: " + repr(home.monsters[0].health))

