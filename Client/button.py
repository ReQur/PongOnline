import pygame

from colors import Color


class Button:
    label = None
    xsize = None
    ysize = None
    bordercolor = None
    constbordercolor = None
    backgroundcolor = None
    borderwidth = None
    X = None
    Y = None
    Hover = False
    prevHover = False
    hovercolor = None


    def __init__(self, label, bordercolor, backgroundcolor, borderwidth, hovercolor = Color.WHITE):
        self.label = label
        labelsize = self.label.font.size(self.label.text)
        self.xsize = labelsize[0] * 1.2
        self.ysize = labelsize[1] * 1.4
        self.bordercolor = bordercolor
        self.constbordercolor = bordercolor
        self.backgroundcolor = backgroundcolor
        self.borderwidth = borderwidth
        self.hovercolor = hovercolor


    def draw(self, screen, X, Y, point = 'left'):
        if not self.prevHover and self.Hover:
            self.label.hovered(self.hovercolor)
            self.bordercolor = self.hovercolor
            self.prevHover = True
        elif self.prevHover and not self.Hover:
            self.label.hovered(self.hovercolor, hover=False)
            self.bordercolor = self.constbordercolor
            self.prevHover = False

        labelsize = self.label.font.size(self.label.text)
        if point == 'center':
            self.X = X - self.xsize / 2
            self.Y = Y - self.ysize / 2
            pygame.draw.rect(screen, self.backgroundcolor,
                             (self.X, self.Y, self.xsize, self.ysize))
            pygame.draw.rect(screen, self.bordercolor,
                             (self.X, self.Y, self.xsize, self.ysize), 7)
            screen.blit(self.label.surface, (X - labelsize[0] / 2, Y - labelsize[1] / 2))