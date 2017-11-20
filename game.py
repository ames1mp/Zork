########################################################################
# @author Mike Ames
# @author Phil Garza
########################################################################
from world import World
import pygame

########################################################################
#Game class. The GUI representation of the game's state.
########################################################################
class Game:

    ####################################################################
    # Constructor. Sets up PyGame, the window, loads assets, defines
    # constants.
    ####################################################################
    def __init__(self):
        self.world = World()

        self.windowWidth = 1600
        self.windowHeight = 900

        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.lightblue = (135, 206, 250)

        pygame.init()
        pygame.display.set_caption('Zork')
        self.spriteStore = {}
        self.gameDisplay = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        self.clock = pygame.time.Clock()
        #Assets
        self.bg = self.getImage('assets/background.png')
        self.font = pygame.font.SysFont(None, 25)
        self.pdown = [self.getImage('assets/wd1.png'), self.getImage('assets/wd2.png')]
        self.pup = [self.getImage('assets/wu1.png'), self.getImage('assets/wu2.png')]
        self.pleft = [self.getImage('assets/wl1.png'), self.getImage('assets/wl2.png')]
        self.pright = [self.getImage('assets/wr1.png'), self.getImage('assets/wr2.png')]
        self.werewolf = self.getImage('assets/werewolf.png')
        self.zombie = self.getImage('assets/zombie.png')
        self.ghoul = self.getImage('assets/ghoul.png')
        self.vampire = self.getImage('assets/vampire.png')
        self.person = self.getImage('assets/person.png')
        self.battleBG = self.getImage('assets/battleBG.png')


        self.townGrid = [[[320, 225], [640, 225], [960, 225], [1280, 225], [1600, 225]],
                         [[320, 450], [640, 450], [960, 450], [1280, 450], [1600, 450]],
                         [[320, 675], [640, 675], [960, 675], [1280, 675], [1600, 675]],
                         [[320, 900], [640, 900], [960, 900], [1280, 900], [1600, 900]],
                         ]

        self.colLen = 320
        self.rowLen = 225
        self.playerGridRow = 0
        self.playerGridCol = 0
        self.currentHouse = self.world.neighborhood.homes[self.playerGridRow][self.playerGridCol]

        self.gameOver = False

    # game loop structure adapted from a video series: https://youtu.be/PzG-fnci8uE
    ########################################################################
    # Run method. The main game loop. Updates the game's state and view.
    ########################################################################
    def run(self):
        gameExit = False
        FPS = 13
        playerX = 200
        playerY = 100
        playerDirection = "s"
        playerXChange = 0
        playerYChange = 0
        counter = 0
        held = False
        movementRate = 37
        onWorldMap = True
        inBattle = False
        player = self.getImage("assets/wd2.png")
        battleRoundOngoing = False

        while not gameExit:
            self.clock.tick(FPS)

            while self.gameOver:
                self.gameDisplay.fill(self.black)
                self.printToScreen("Game Over", self.red, 800, 300)
                self.printToScreen("Play again?:   [Y]   [N]", self.red, 800, 400)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_y:
                            self.world = World()
                            onWorldMap = True
                            inBattle = False
                            self.gameOver = False
                            self.run()
                        if event.key == pygame.K_n:
                            pygame.quit()
                            quit()

            if onWorldMap:
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                            playerDirection = "n"
                            held = True
                            playerYChange = -movementRate
                        if event.key == pygame.K_a:
                            playerDirection = "w"
                            held = True
                            playerXChange = -movementRate

                        if event.key == pygame.K_s:
                            playerDirection = "s"
                            held = True
                            playerYChange = movementRate

                        if event.key == pygame.K_d:
                            playerDirection = "e"
                            held = True
                            playerXChange = movementRate

                        if event.key == pygame.K_RETURN:
                            if self.currentHouse.numBaddies > 0:
                                onWorldMap = False
                                inBattle = True
                                continue
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_w or event.key == pygame.K_s:
                            playerYChange = 0
                            held = False
                        if event.key == pygame.K_a or event.key == pygame.K_d:
                            playerXChange = 0
                            held = False

                playerX += playerXChange
                playerY += playerYChange

                if playerDirection == "s" and held == True:
                    counter = (counter + 1) % 2
                    player = self.pdown[counter]
                elif playerDirection == "w" and held == True:
                    counter = (counter + 1) % 2
                    player = self.pleft[counter]
                elif playerDirection == "e" and held == True:
                    counter = (counter + 1) % 2
                    player = self.pright[counter]
                elif playerDirection == "n" and held == True:
                    counter = (counter + 1) % 2
                    player = self.pup[counter]

                self.updateLoc(playerDirection, playerX, playerY)
                self.currentHouse = self.world.neighborhood.homes[self.playerGridRow][self.playerGridCol]

                self.gameDisplay.blit(self.bg, (0, 0))
                self.gameDisplay.blit(player, (playerX, playerY))

                self.printNumMonsters()
                self.printHomeInfo(playerX, playerY)
                self.printToScreen("Press [ENTER] to enter a home", self.red, 750, 0)

                pygame.display.update()

            #Battle Screen
            if inBattle:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_0:
                            self.battleRound(self.world.player.inventory[0])
                            battleRoundOngoing == True
                        if event.key == pygame.K_1 and len(self.world.player.inventory) >= 2:
                            self.battleRound(self.world.player.inventory[1])
                            battleRoundOngoing == True
                        if event.key == pygame.K_2 and len(self.world.player.inventory) >= 3:
                            self.battleRound(self.world.player.inventory[2])
                            battleRoundOngoing == True
                        if event.key == pygame.K_3 and len(self.world.player.inventory) >= 4:
                            self.battleRound(self.world.player.inventory[3])
                            battleRoundOngoing == True
                        if event.key == pygame.K_4 and len(self.world.player.inventory) >= 5:
                            self.battleRound(self.world.player.inventory[4])
                            battleRoundOngoing == True
                        if event.key == pygame.K_5 and len(self.world.player.inventory) >= 6:
                            self.battleRound(self.world.player.inventory[5])
                            battleRoundOngoing == True
                        if event.key == pygame.K_6 and len(self.world.player.inventory) >= 7:
                            self.battleRound(self.world.player.inventory[6])
                            battleRoundOngoing == True
                        if event.key == pygame.K_7 and len(self.world.player.inventory) >= 8:
                            self.battleRound(self.world.player.inventory[7])
                            battleRoundOngoing == True
                        if event.key == pygame.K_8 and len(self.world.player.inventory) >= 9:
                            self.battleRound(self.world.player.inventory[8])
                            battleRoundOngoing == True
                        if event.key == pygame.K_9 and len(self.world.player.inventory) == 10:
                            self.battleRound(self.world.player.inventory[9])
                            battleRoundOngoing == True

                self.gameDisplay.fill(self.black)
                self.gameDisplay.blit(self.battleBG, (0, 200))
                self.gameDisplay.fill(self.white, rect=[650, 700, 10, 250])
                self.gameDisplay.fill(self.white, rect=[650, 700, 250, 10])
                self.gameDisplay.fill(self.white, rect=[900, 700, 10, 250])
                self.gameDisplay.fill(self.lightblue, rect=[660, 710, 240, 240])
                self.printToScreen("Mike", self.white, 680, 730)
                self.printToScreen("HP: " + repr(self.world.player.health), self.white, 680, 790)
                self.showMonsters()
                self.printItems()

                self.clock.tick(5)
                pygame.display.update()

    pygame.quit()

    ########################################################################
    # Prints text to the screen. Take a message, and font color, and
    # coordinates to print the text at.
    ########################################################################
    # adapted from https://youtu.be/PzG-fnci8uE
    def printToScreen(self, msg, color, x, y):
        text = self.font.render(msg, True, color)
        self.gameDisplay.blit(text, (x, y))

    ########################################################################
    # Prints the number of monsters in the neighborhood to the screen.
    ########################################################################
    def printNumMonsters(self):
        numMonsters = self.world.neighborhood.numMonsters
        msg = repr(numMonsters) + " monsters remaining"
        self.printToScreen(msg, self.red, 1400, 10)

    ########################################################################
    # A sprite store. Loads images and saves them to a dictionary. Returns
    # images if the have already been loaded.
    ########################################################################
    # from https://stackoverflow.com/questions/17615447/pre-loading-images-pygame
    def getImage(self, key):
        if key not in self.spriteStore:
            self.spriteStore[key] = pygame.image.load(key)
        return self.spriteStore[key]

    ########################################################################
    # Updates a record of the player's location on the world map screen.
    ########################################################################
    def updateLoc(self, playerDirection, playerX, playerY):
        if playerDirection == "e" or playerDirection == "w":
            if  playerX > 0 and playerX < self.colLen:
                self.playerGridCol = 0
            elif playerX > self.colLen and playerX < self.colLen * 2:
                self.playerGridCol = 1
            elif playerX > self.colLen*2 and playerX < self.colLen * 3:
                self.playerGridCol = 2
            elif playerX > self.colLen*3 and playerX < self.colLen * 4:
                self.playerGridCol = 3
            elif playerX > self.colLen*4 and playerX < self.colLen * 5:
                self.playerGridCol = 4

        elif playerDirection == "n" or playerDirection == "s":
            if  playerY > 0 and playerY < self.rowLen:
                self.playerGridRow = 0
            elif playerY > self.rowLen and playerY < self.rowLen * 2:
                self.playerGridRow = 1
            elif playerY > self.rowLen*2 and playerY < self.rowLen * 3:
                self.playerGridRow = 2
            elif playerY > self.rowLen*3 and playerY < self.rowLen * 4:
                self.playerGridRow = 3

    ########################################################################
    # Prints text to the screen displaying the number of monsters in a house.
    ########################################################################
    def printHomeInfo(self, playerX, playerY):
        msg = ""
        color = (0, 0, 0)
        home = self.world.neighborhood.homes[self.playerGridRow][self.playerGridCol]
        numMonsters = home.numBaddies
        if numMonsters == 0:
            msg = "House Clear!"
            color = self.green
        else:
            msg = repr(numMonsters) + " monsters infest this house"
            color = self.red
        x = playerX - 50
        y = playerY - 50
        self.printToScreen(msg, color, x, y)

    ########################################################################
    # Renders monsters to the battle screen.
    ########################################################################
    def showMonsters(self):
        monsters = self.currentHouse.monsters
        monsterSpacing = 120
        monsterX = 0
        monsterY = 400

        for monster in monsters:
            if monster.type == "zombie":
                self.gameDisplay.blit(self.zombie, (monsterX, monsterY))
            elif monster.type == "ghoul":
                self.gameDisplay.blit(self.ghoul, (monsterX, monsterY))
            elif monster.type == "vampire":
                self.gameDisplay.blit(self.vampire, (monsterX, monsterY))
            elif monster.type == "werewolf":
                self.gameDisplay.blit(self.werewolf, (monsterX, monsterY))
            elif monster.type == "person":
                self.gameDisplay.blit(self.person, (monsterX, monsterY))
            monsterX += monsterSpacing

    ########################################################################
    # Prints a list of the player's weapons to the screen
    ########################################################################
    def printItems(self):
        x = 20
        y = 20
        xSpacing = 250
        ySpacing = 30
        itemNo = 0

        items = self.world.player.inventory

        for item in items:
            self.printToScreen("[" + repr(itemNo) + "] to use: " + item.type + " x " + repr(item.uses), self.white, x, y)
            x += xSpacing
            itemNo += 1
            if x > 800:
                x = 20
                y += ySpacing

    ########################################################################
    # Executes the battle logic and updates the view accordingly.
    ########################################################################
    def battleRound(self, weapon):
        displayBattleText = True
        battleText = []
        battleTextIndex = 0
        battleWon = False
        self.gameDisplay.fill(self.black)
        self.gameDisplay.blit(self.battleBG, (0, 200))
        self.gameDisplay.fill(self.white, rect=[650, 700, 10, 250])
        self.gameDisplay.fill(self.white, rect=[650, 700, 250, 10])
        self.gameDisplay.fill(self.white, rect=[900, 700, 10, 250])
        self.gameDisplay.fill(self.lightblue, rect=[660, 710, 240, 240])
        self.printToScreen("Mike", self.white, 680, 730)
        self.printToScreen("HP: " + repr(self.world.player.health), self.white, 680, 790)
        self.printToScreen("You used: " + weapon.type, self.green, 20, 20)
        self.showMonsters()

        monsters = self.currentHouse.monsters
        player = self.world.player

        for monster in monsters:
            name = monster.type
            info = monster.defend(player.attack(weapon))

            battleText.append(repr(info["damage"]) + "HP damage to " + name)
            if info['dead']:
                battleText.append(name + " was defeated")
        for monster in monsters:
            player.defend(monster.attack())
            battleText.append(monster.type + " attacked for " + repr(monster.attackPower) + " HP damage!")
        if player.health <= 0:
            battleText.append("You were defeated!!")
        if self.currentHouse.numBaddies == 0:
            battleText.append("YOU WON!")
            battleWon = True

        pygame.display.update()
        while displayBattleText:
            self.gameDisplay.fill(self.black)
            self.gameDisplay.blit(self.battleBG, (0, 200))
            self.gameDisplay.fill(self.white, rect=[650, 700, 10, 250])
            self.gameDisplay.fill(self.white, rect=[650, 700, 250, 10])
            self.gameDisplay.fill(self.white, rect=[900, 700, 10, 250])
            self.gameDisplay.fill(self.lightblue, rect=[660, 710, 240, 240])
            self.printToScreen("Mike", self.white, 680, 730)
            self.printToScreen("HP: " + repr(self.world.player.health), self.white, 680, 790)
            self.showMonsters()


            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if battleTextIndex < len(battleText):
                            self.printToScreen(battleText[battleTextIndex], self.white, 20, 20)
                            battleTextIndex += 1
                            pygame.display.update()
                        elif player.health <= 0:
                            self.gameOver = True
                            inBattle = False
                            self.run()
                        else:
                            displayBattleText = False
        if battleWon:
            self.inBattle = False
            self.onWorldMap = True
            pygame.display.update()
            self.run()


class Driver:
    if __name__ == '__main__':
        g = Game()
        g.run()
