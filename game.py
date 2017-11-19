from world import World
import pygame

class Game:

    def __init__(self):
        self.world = World()

        self.windowWidth = 1600
        self.windowHeight = 900

        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

        pygame.init()
        pygame.display.set_caption('Zork')
        self.spriteStore = {}
        self.gameDisplay = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        self.clock = pygame.time.Clock()
        self.bg = self.getImage('assets/background.png')
        self.font = pygame.font.SysFont(None, 25)
        self.pdown = [self.getImage('assets/wd1.png'), self.getImage('assets/wd2.png')]
        self.pup = [self.getImage('assets/wu1.png'), self.getImage('assets/wu2.png')]
        self.pleft = [self.getImage('assets/wl1.png'), self.getImage('assets/wl2.png')]
        self.pright = [self.getImage('assets/wr1.png'), self.getImage('assets/wr2.png')]




    # game loop structure adapted from a video series: https://youtu.be/PzG-fnci8uE
    def run(self):
        gameExit = False
        gameOver = False
        FPS = 30
        playerX = 800
        playerY = 450


        while not gameExit:

            while gameOver:
                pass

            # Handle user input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_w:
                        playerX = 10
                    if event.type == pygame.K_a:

                    if event.type == pygame.K_s:

                    if event.type == pygame.K_d:

                    if event.type == pygame.K_RETURN:

            self.gameDisplay.blit(self.bg, (0, 0))

            self.printNumMonsters()
            pygame.display.update()

        self.clock.tick(FPS)


    pygame.quit()

    # adapted from https://youtu.be/PzG-fnci8uE
    def printToScreen(self, msg, color, x, y):
        text = self.font.render(msg, True, color)
        self.gameDisplay.blit(text, (x, y))

    def printNumMonsters(self):
        numMonsters = self.world.neighborhood.numMonsters
        msg = repr(numMonsters) + " monsters remaining"
        self.printToScreen(msg, self.red, 1400, 10)

    # from https://stackoverflow.com/questions/17615447/pre-loading-images-pygame
    def getImage(self, key):
        if not key in self.spriteStore:
            self.spriteStore[key] = pygame.image.load(key)
        return self.spriteStore[key]

class Driver:
    if __name__ == '__main__':
        g = Game()
        g.run()
