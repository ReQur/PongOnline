import pygame

from label import Label
from button import Button
from colors import Color
from textinput import TextInput

class Renderer:
    screen = None
    largeFont = None
    smallFont = None
    mediumFont = None

    __windowsize = [800, 600]
    __windowname = 'Pong!'

    __fontfamaly = 'Source/PressStart2P.ttf'
    __large_fontsize = 130
    __small_fontsize = 30
    __medium_fontsize = 50

    PongTitle = None

    connetionText = None

    quitButton = None
    playButton = None

    backButton = None
    connectButton = None

    addressBox = None

    def __init__(self):
        self.screen = pygame.display.set_mode(self.__windowsize)
        pygame.display.set_caption(self.__windowname)

        pygame.font.init()
        self.largeFont = pygame.font.Font(self.__fontfamaly, self.__large_fontsize)
        self.smallFont = pygame.font.Font(self.__fontfamaly, self.__small_fontsize)
        self.mediumFont = pygame.font.Font(self.__fontfamaly, self.__medium_fontsize)

        self.PongTitle = Label('Pong', Color.WHITE, self.largeFont)
        self.connetionText = Label('Waiting second player', Color.WHITE, self.smallFont)

        self.quitButton = Button(Label('Quit', Color.BLACK, self.smallFont), Color.BLACK, Color.COFFEE, 7)
        self.playButton = Button(Label('Play', Color.BLACK, self.smallFont), Color.BLACK, Color.COFFEE, 7)
        self.backButton = Button(Label('Back', Color.BLACK, self.smallFont), Color.BLACK, Color.COFFEE, 7)

        self.connectButton = Button(Label('Connect', Color.BLACK, self.smallFont), Color.BLACK, Color.COFFEE, 7)

        self.addressBox = TextInput(self.smallFont, Color.WHITE, Color.BLACK, placeholder='localhost', numeric=True)



    def run_render(self, point, playerLeft, playerRight):
        self.screen.fill(Color.DARK_GREY_RED_BROWN)

        playerLeftScoreTextSize = self.largeFont.size(str(playerLeft.score))
        playerLeftScoreTextSurface = self.largeFont.render(str(playerLeft.score), False, Color.COFFEE)
        self.screen.blit(playerLeftScoreTextSurface, (400 - playerLeftScoreTextSize[0] - 30, 130))

        playerRightScoreTextSurface = self.largeFont.render(str(playerRight.score), False, Color.COFFEE)
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

        self.PongTitle.draw(self.screen, 400, 200, 'center')

        self.playButton.draw(self.screen, 400, 380, 'center')
        self.quitButton.draw(self.screen, 400, 450, 'center')

        pygame.display.flip()


    def enter_to_lobby(self):
        self.screen.fill(Color.DARK_GREY_RED_BROWN)

        pygame.draw.rect(self.screen, Color.WHITE,
                         (50, 30, 700, 540), 7)

        self.backButton.draw(self.screen, 70, 50)

        self.addressBox.draw(self.screen, 400, 300, 'center')

        self.connectButton.draw(self.screen, 400, 400, 'center')



        pygame.display.flip()


    def connetion_wait(self):
        self.screen.fill(Color.DARK_GREY_RED_BROWN)

        pygame.draw.rect(self.screen, Color.WHITE,
                         (50, 30, 700, 540), 7)

        self.connetionText.draw(self.screen, 400, 300, 'center')

        pygame.display.flip()




