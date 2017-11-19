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

# class Driver:
#
#     if __name__ == '__main__':
#         attackData = {"playerBaseAttackPower": 10,
#                      "playerModifiedAttackPower": 700,
#                      "weaponType": "hersheykiss"}
#
#         n = Neighborhood()
#
#         print("There are: " + repr(len(n.homes)) + " homes")
#         print(n.numMonsters)

        # for m in n.homes[0][0].monsters:
        #     m.defend(attackData)
        #     print("Monsters remaining: " + repr(len(n.homes[0][0].monsters)))
        # n.homes[0][0].monsters[0].defend(attackData)
        # print("Monsters remaining: " + repr(len(n.homes[0][0].monsters)))
        # print("There are: " + repr(len(n.homes)) + " homes")
        #
        # for i in range(5):
        #     for j in range(5):
        #         print(n.homes[i][j].row)
