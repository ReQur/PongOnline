class Player:
    width = 10
    height = 80
    x = 0
    y = 0

    dY = 4

    hBorder = 0
    topBorder = 0
    bottomBorder = 0

    borderRadius = 60
    color = (255, 255, 255)
    side = ""

    score = 0

    def __init__(self, player_side : str, score):
        self.y = 300 - self.height / 2
        self.x = 100 - self.width / 2 if player_side == "LEFT" else 700 - self.width / 2

        self.hBorder = self.x + self.width if player_side == "LEFT" else self.x
        self.topBorder = self.y
        self.bottomBorder = self.y + self.height

        self.side = player_side

        self.score = score

    def update_pos(self, newY):
        self.y = newY
        self.topBorder = self.y
        self.bottomBorder = self.y + self.height
