########################################################################
# @author Mike Ames
# @author Phil Garza
########################################################################
import random
from observer import Observer
from observable import Observable
from mob_factory import Mob, MonsterTypes

########################################################################
# Home Class. Generates and stores a list of monsters. Observes the
# monster class and removes monsters from the list when they die.
# Observed by the world class. Notifies the world class when the number
# of monsters it contains changes.
########################################################################
class Home(Observable, Observer):

    ####################################################################
    # Constructor. Generates a random number of monsters and stores them
    # in a list.
    ####################################################################
    def __init__(self):
        super().__init__()
        random.seed()
        numMonsters = random.randrange(1, 11)

        self.monsters = []

        for i in range(numMonsters):
            # represents the type of monster to be created
            monsterRand = random.randrange(1, 5)

            # get the name of the monster defined in the enum in the
            # mob_factory module and use it
            # to create a new monster and add it to the home's list
            monster = Mob.factory(MonsterTypes(monsterRand).name)
            self.monsters.append(monster)
            monster.addObserver(self)

        self.numBaddies = len(self.monsters)

    #####################################################################
    # Update method. When invoked by the monster class on the monster's
    # death, this method removes the monster from the home's list. It
    # then notifies the world class the number of monsters in the home
    # has decreased.
    #####################################################################
    def update(self, other):
        self.monsters.remove(other)
        self.numBaddies -= 1
        self.monsters.append(Mob.factory("person"))
        super().update(self)

