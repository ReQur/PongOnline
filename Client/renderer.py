import pygame

class Renderer:
    screen = None
    scoreFont = None

    __windowsize = [800, 600]
    __windowname = 'Pong!'

    __fontsize = 150
    __fontfamaly = 'Consolas'


    def __init__(self):
        self.screen = pygame.display.set_mode(self.__windowsize)
        pygame.display.set_caption(self.__windowname)

        pygame.font.init()
        self.scoreFont = pygame.font.SysFont(self.__fontfamaly, self.__fontsize)


    def run_render(self, point, playerLeft, playerRight):
        self.screen.fill((50, 35, 35))

        playerLeftScoreTextSize = self.scoreFont.size(str(playerLeft.score))
        playerLeftScoreTextSurface = self.scoreFont.render(str(playerLeft.score), False, (60, 42, 42))
        self.screen.blit(playerLeftScoreTextSurface, (400 - playerLeftScoreTextSize[0] - 30, 130))

        playerRightScoreTextSurface = self.scoreFont.render(str(playerRight.score), False, (60, 42, 42))
        self.screen.blit(playerRightScoreTextSurface, (400 + 30, 130))

        pygame.draw.rect(self.screen, playerLeft.color, \
                         pygame.Rect(playerLeft.x, playerLeft.y, playerLeft.width, playerLeft.height),
                         border_radius=playerLeft.borderRadius)
        pygame.draw.rect(self.screen, playerRight.color, \
                         pygame.Rect(playerRight.x, playerRight.y, playerRight.width, playerRight.height),
                         border_radius=playerRight.borderRadius)

        pygame.draw.rect(self.screen, (255, 255, 255),
                         (50, 30, 700, 540), 7)
        pygame.draw.line(self.screen, (255, 255, 255),
                         [400, 30], [400, 570], 3)

        pygame.draw.circle(self.screen, point.color, (point.x, point.y), point.diameter)

        pygame.display.flip()




