class Label:
    surface = None
    font = None
    color = None
    text = None


    def __init__(self, text, color, font):
        self.text = text
        self.color = color
        self.font = font
        self.surface = self.font.render(self.text, True, self.color)


    def draw(self, screen, X, Y, point = 'left'):
        size = self.font.size(self.text)
        if point == 'center':
            screen.blit(self.surface, (X - size[0]/2, 130))


    def hovered(self, hoveredcolor = color,  hover = True):
        if hover:
            self.surface = self.font.render(self.text, True, hoveredcolor)
        else:
            self.surface = self.font.render(self.text, True, self.color)