import pygame

from label import Label
from button import Button
from colors import Color

class Renderer:
    screen = None
    scoreFont = None
    buttonFont = None

    __windowsize = [800, 600]
    __windowname = 'Pong!'

    __fontfamaly = 'Source/PressStart2P.ttf'
    __score_fontsize = 130
    __buttons_fontsize = 30

    PongTitle = None

    quitButton = None
    playButton = None

    def __init__(self):
        self.screen = pygame.display.set_mode(self.__windowsize)
        pygame.display.set_caption(self.__windowname)

        pygame.font.init()
        self.scoreFont = pygame.font.Font(self.__fontfamaly, self.__score_fontsize)
        self.buttonFont = pygame.font.Font(self.__fontfamaly, self.__buttons_fontsize)

        self.PongTitle = Label('Pong', Color.WHITE, self.scoreFont)

        self.quitButton = Button(Label('Quit', Color.BLACK, self.buttonFont), Color.BLACK, Color.COFFEE, 7)
        self.playButton = Button(Label('Play', Color.BLACK, self.buttonFont), Color.BLACK, Color.COFFEE, 7)



    def run_render(self, point, playerLeft, playerRight):
        self.screen.fill(Color.DARK_GREY_RED_BROWN)

        playerLeftScoreTextSize = self.scoreFont.size(str(playerLeft.score))
        playerLeftScoreTextSurface = self.scoreFont.render(str(playerLeft.score), False, Color.COFFEE)
        self.screen.blit(playerLeftScoreTextSurface, (400 - playerLeftScoreTextSize[0] - 30, 130))

        playerRightScoreTextSurface = self.scoreFont.render(str(playerRight.score), False, Color.COFFEE)
        self.screen.blit(playerRightScoreTextSurface, (400 + 30, 130))

        pygame.draw.rect(self.screen, playerLeft.color, \
                         pygame.Rect(playerLeft.x, playerLeft.y, playerLeft.width, playerLeft.height),
                         border_radius=playerLeft.borderRadius)
        pygame.draw.rect(self.screen, playerRight.color, \
                         pygame.Rect(playerRight.x, playerRight.y, playerRight.width, playerRight.height),
                         border_radius=playerRight.borderRadius)

        pygame.draw.rect(self.screen, Color.WHITE,
                         (50, 30, 700, 540), 7)
        pygame.draw.line(self.screen, Color.WHITE,
                         [400, 30], [400, 570], 3)

        pygame.draw.circle(self.screen, point.color, (point.x, point.y), point.diameter)

        pygame.display.flip()


    def main_menu(self):
        self.screen.fill(Color.DARK_GREY_RED_BROWN)

        pygame.draw.rect(self.screen, Color.WHITE,
                         (50, 30, 700, 540), 7)

        self.PongTitle.draw(self.screen, 400, 130, 'center')

        self.playButton.draw(self.screen, 400, 380, 'center')
        self.quitButton.draw(self.screen, 400, 450, 'center')

        pygame.display.flip()




