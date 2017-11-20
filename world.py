########################################################################
# @author Mike Ames
# @author Phil Garza
########################################################################
from player import Player
from neighborhood import Neighborhood
from observer import Observer

########################################################################
# World Class. Contains the neighborhood and the player. Observes homes
# and updates the monster count in the neighborhood class.
########################################################################
class World(Observer):

    ########################################################################
    # Constructor. Generates the neighborhood and the player.
    ########################################################################
    def __init__(self):
        super().__init__()
        self.player = Player()
        self.neighborhood = Neighborhood(5, 4)
        for row in self.neighborhood.homes:
            for home in row:
                home.addObserver(self)

    ########################################################################
    # Update method. Updates the count of monsters in the neighborhood when
    # invoked by the Home class.
    ########################################################################
    def update(self, other):
        self.neighborhood.numMonsters -= 1
