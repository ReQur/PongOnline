class Player:
    width = 10
    height = 80
    x = 0
    y = 0
    dY = 4
    borderRadius = 60
    color = (255, 255, 255)
    score = 0

    def __init__(self):
        pass

    # def __init__(self, x, y, width, height, borderRadius, color, score):
    #     self.y = y
    #     self.x = x
    #     self.width = width
    #     self.height = height
    #     self.borderRadius = borderRadius
    #     self.color = color
    #     self.score = score

    def move_up(self):
        if(self.y  > 30):
            self.y -= self.dY

        self.topBorder = self.y
        self.bottomBorder = self.y + self.height

    def move_down(self):
        if(self.y  < 570 - self.height):
            self.y += self.dY

        self.topBorder = self.y
        self.bottomBorder = self.y + self.height
