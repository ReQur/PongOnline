from vector import Vector


class Point:
    diameter = 6
    x = 0
    y = 0
    hBorder = 0

    velocity = 3
    L = Vector(1, 0)

    color = (255, 255, 255)

    def __init__(self):
        self.x = 400
        self.y = 300
        self.hBorder = self.x + self.diameter / 2 if self.L.x > 0 else self.x
        self.color = (255, 255, 255)

    def collision_check(self, player):
        return ((player.side != "LEFT" and player.hBorder + player.width >= self.hBorder >= player.hBorder)
                or (player.side == "LEFT" and player.hBorder - player.width <= self.hBorder <= player.hBorder)) \
                and player.topBorder <= self.y <= player.bottomBorder

    def reflection_calc(self, player):
        zeroY = player.topBorder + player.height/2
        relativeY = self.y - zeroY
        zeroX = player.hBorder

        self.L = Vector.calc_from_reflect(zeroX - player.height/4 if player.side == "LEFT" else zeroX + player.height/4,
                                     zeroX, 0, relativeY)

    def wall_collision_check(self):
        return (self.y <= 30 + self.diameter/2) or (self.y >= 570 - self.diameter/2)

    def tick_calc(self, playerLeft, playerRight):
        result = {
            "Reflect" : (True, False),
            "Reset" : (False, True)
        }

        if self.collision_check(playerLeft):
            self.reflection_calc(playerLeft)
            self.move()
            return result["Reflect"]
        elif self.collision_check(playerRight):
            self.reflection_calc(playerRight)
            self.move()
            return result["Reflect"]

        if self.wall_collision_check():
            self.L.y *= -1
            self.move()
            return result["Reflect"]

        if self.x < playerLeft.x - 50 or self.x > playerRight.x + 50:
            self.color = (255, 180, 180)
            return result["Reset"]

        self.move()

    def move(self):
        self.x += self.L.x * self.velocity
        self.y += self.L.y * self.velocity
        self.hBorder = self.x + self.diameter / 2 if self.L.x > 0 else self.x

