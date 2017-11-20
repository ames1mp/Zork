########################################################################
# @author Mike Ames
# @author Phil Garza
########################################################################
from home import Home

########################################################################
# Neighborhood class. Hold a 2D list of all of the houses in the game.
########################################################################
class Neighborhood:

    ########################################################################
    # Constructor. Generates homes and places them in a 2D list. Keeps track
    # of the number of monsters in the neighborhood.
    ########################################################################
    def __init__(self, width, height):
        super().__init__
        self.width = width
        self.height = height
        self.homes = []
        self.numMonsters = 0

        for row in range(self.height):
            row = []
            self.homes.append(row)
            for col in range(self.width):
                home = Home()
                self.numMonsters += len(home.monsters)
                row.append(home)
