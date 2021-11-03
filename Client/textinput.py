import pygame
from colors import Color

class TextInput:
    text = ''
    placeholder = None
    placeholdercolor = None
    maxtextlen = None
    font = None
    fontcolor = None
    surface = None
    backgroundcolor = None
    constbordercolor = None
    bordercolor = None
    activeboredercolor = None
    Hover = False
    prevHover = False
    active = False
    xsize = None
    ysize = None
    X = None
    Y = None
    numeric = None

    IPchars = '0123456789.'

    def __init__(self, font, fontcolor, backgrondcolor, bordercolor=Color.GREY, activebordercolor=Color.WHITE,
                 placeholder=None, maxtextlen=15, numeric = False):
        self.font = font
        self.fontcolor = fontcolor
        self.backgroundcolor = backgrondcolor
        self.bordercolor = backgrondcolor
        self.placeholdercolor = bordercolor
        self.constbordercolor = bordercolor
        self.activeboredercolor = activebordercolor
        self.placeholder = placeholder
        self.maxtextlen = maxtextlen
        self.numeric = numeric

        if self.placeholder != None:
            self.surface = self.font.render(self.placeholder, True, self.placeholdercolor)

        maxstr = ''
        for i in range(maxtextlen):
            maxstr += '0'

        self.xsize, self.ysize = self.font.size(maxstr)
        self.xsize *= 1.1
        self.ysize *= 1.4


    def draw(self, screen, X, Y, point = 'left'):
        if not self.active:
            if not self.prevHover and self.Hover:
                self.bordercolor = self.constbordercolor
                self.prevHover = True
            elif self.prevHover and not self.Hover:
                self.bordercolor = self.backgroundcolor
                self.prevHover = False

        if point == 'center':
            self.X = X - self.xsize / 2
            self.Y = Y - self.ysize / 2
            pygame.draw.rect(screen, self.backgroundcolor,
                             (self.X, self.Y, self.xsize, self.ysize))
            pygame.draw.rect(screen, self.bordercolor,
                             (self.X, self.Y, self.xsize, self.ysize), 7)
            screen.blit(self.surface, (X - self.xsize / (2*1.1), Y - self.ysize / (2*1.4)))
        elif point == 'left':
            self.X = X
            self.Y = Y
            pygame.draw.rect(screen, self.backgroundcolor,
                             (self.X, self.Y, self.xsize, self.ysize))
            pygame.draw.rect(screen, self.bordercolor,
                             (self.X, self.Y, self.xsize, self.ysize), 7)
            screen.blit(self.surface, (X - self.xsize*0.1, Y - self.ysize*0.2))

    def check_cursor_hover(self, cursor_pos):
        if self.X == None: return
        if cursor_pos[0] < self.X or cursor_pos[0] > self.X + self.xsize \
                or cursor_pos[1] < self.Y or cursor_pos[1] > self.Y + self.ysize:
            self.Hover = False
        else:
            self.Hover = True

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.Hover:
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.bordercolor = self.activeboredercolor if self.active else self.constbordercolor
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if self.numeric:
                        if event.unicode in self.IPchars:
                            self.text += event.unicode
                    else:
                        self.text += event.unicode
                # Re-render the text.
                if self.text != '':
                    self.surface = self.font.render(self.text, True, self.fontcolor)
                elif self.placeholder != None:
                    self.surface = self.font.render(self.placeholder, True, self.placeholdercolor)