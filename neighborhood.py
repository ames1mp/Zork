from home import Home


class Neighborhood:

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
