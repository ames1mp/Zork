import random

# Factory code adapted from: http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html


class Weapon(object):
    def factory(monsterType):
        if monsterType == "hersheykiss": return HersheyKiss()
        if monsterType == "sourstraw": return SourStraw()
        if monsterType == "chocolatebar": return ChocolateBar()
        if monsterType == "nerdbomb": return NerdBomb()
        assert 0, "Invalid type: " + monsterType
    factory = staticmethod(factory)


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