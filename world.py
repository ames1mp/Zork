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
        self.neighborhood.numMonsters -= 1
