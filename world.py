from player import Player
from neighborhood import Neighborhood
from observer import Observer


class World(Observer):

    def __init__(self):
        super().__init__()
        self.player = Player()
        self.neighborhood = Neighborhood(5, 4)
        for row in self.neighborhood.homes:
            for home in row:
                home.addObserver(self)

    def update(self, other):
        print("UPDATE!")
        self.neighborhood.numMonsters -= 1


# class Driver:
#
#     if __name__ == '__main__':
#         attackData = {"playerBaseAttackPower": 10,
#                       "playerModifiedAttackPower": 1000,
#                       "weaponType": "hersheykiss"}
#
#         w = World()
#         player = w.player
#         currentHome = w.neighborhood.homes[0][0]
#         monster = currentHome.monsters[0]
#
#         print("There are " + repr(w.neighborhood.numMonsters) + " monsters in the hood")
#         monster.defend(attackData)
#         print("There are " + repr(w.neighborhood.numMonsters) + " monsters in the hood")



