########################################################################
# @author Mike Ames
# @author Phil Garza
########################################################################
import random

# Factory code adapted from: http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html

########################################################################
# Weapon Class. The parent class for weapons.
########################################################################
class Weapon(object):

    ########################################################################
    # Factory method which generates a weapon based on the type provided.
    # @return a weapon object.
    ########################################################################
    def factory(weaponType):
        if weaponType == "hersheykiss": return HersheyKiss()
        if weaponType == "sourstraw": return SourStraw()
        if weaponType == "chocolatebar": return ChocolateBar()
        if weaponType == "nerdbomb": return NerdBomb()
        assert 0, "Invalid type: " + weaponType
    factory = staticmethod(factory)

########################################################################
# Weapon classes. The child classes of Weapon. Sets the weapons' type
# attack modifier and number of uses
########################################################################
class HersheyKiss(Weapon):
    def __init__(self):
        self.type = "HersheyKiss"
        self.attackMod = 1
        self.uses = float('inf')


class SourStraw(Weapon):
    def __init__(self):
        self.type = "SourStraw"
        random.seed()
        self.attackMod = round(random.uniform(1, 1.75), 2)
        self.uses = 2


class ChocolateBar(Weapon):
    def __init__(self):
        self.type = "ChocolateBar"
        random.seed()
        self.attackMod = round(random.uniform(2, 2.4), 2)
        self.uses = 4


class NerdBomb(Weapon):
    def __init__(self):
        self.type = "NerdBomb"
        random.seed()
        self.attackMod = round(random.uniform(3.5, 5), 2)
        self.uses = 1