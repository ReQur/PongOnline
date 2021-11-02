import pygame

from threading import Thread
from time import sleep, time_ns

from player import Player
from point import Point
from connection import Connection
from renderer import Renderer

class Game:
    FPS = 60
    clock = None

    point = None
    playerLeft = None
    playerRight = None

    conn = None
    rend = None

    running = None

    buttons = []



    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.rend = Renderer()
        self.buttons.append(self.rend.quitButton)
        self.buttons.append(self.rend.playButton)


    def __run_init(self):
        self.playerLeft = Player()
        self.playerRight = Player()

        self.conn = Connection('localhost')

        self.point, self.playerLeft, self.playerRight = self.conn.recieve_data(self.playerLeft, self.playerRight, first_tick=True)

        Thread(target=self.conn.send_data, args=[self.playerLeft, self.playerRight]).start()

        self.running = True


    def run(self):
        self.__run_init()
        while self.running:
            self.clock.tick(self.FPS)

            if self.is_close_event():
                self.conn.close()
                self.running = False
                break

            self.point, self.playerLeft, self.playerRight = self.conn.recieve_data(self.playerLeft, self.playerRight)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                {
                    'left': self.playerLeft.move_up,
                    'right': self.playerRight.move_up
                }[self.conn.this_client_player_side]()
            elif keys[pygame.K_DOWN]:
                {
                    'left': self.playerLeft.move_down,
                    'right': self.playerRight.move_down
                }[self.conn.this_client_player_side]()

            self.rend.run_render(self.point, self.playerLeft, self.playerRight)

    def is_close_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
        return False


    def check_cursor_hover(self, cursor_pos):
        for button in self.buttons:
            if cursor_pos[0] < button.X or cursor_pos[0] > button.X + button.xsize \
                    or cursor_pos[1] < button.Y or cursor_pos[1] > button.Y + button.ysize:
                button.Hover=False
            else:
                button.Hover=True

    def main_menu(self):
        self.running = True
        while self.running:
            self.rend.main_menu()

            cursor_pos = pygame.mouse.get_pos()
            self.check_cursor_hover(cursor_pos)

            if self.is_close_event():
                self.running = False
                break


