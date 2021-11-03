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

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.rend = Renderer()


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

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                return None
            if self.rend.addressBox.Hover or self.rend.addressBox.active:
                self.rend.addressBox.handle_event(event)
                self.rend.addressBox.Hover = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.rend.quitButton.Hover:
                    self.rend.quitButton.Hover = False
                    self.rend.quitButton.method()
                elif event.button == 1 and self.rend.playButton.Hover:
                    self.rend.playButton.Hover = False
                    return self.rend.playButton.method
                elif event.button == 1 and self.rend.backButton.Hover:
                    self.rend.backButton.Hover = False
                    return self.rend.backButton.method

    def quit_method(self):
        self.running = False
        pygame.quit()

    def main_menu(self):
        buttons = []
        self.rend.quitButton.method = self.quit_method
        self.rend.playButton.method = self.enter_to_lobby
        buttons.append(self.rend.quitButton)
        buttons.append(self.rend.playButton)
        self.running = True
        while self.running:
            self.rend.main_menu()

            cursor_pos = pygame.mouse.get_pos()

            for button in buttons:
                button.check_cursor_hover(cursor_pos)

            method = self.check_events()
            if method: return method


    def enter_to_lobby(self):
        buttons = []
        self.rend.backButton.method = self.main_menu
        buttons.append(self.rend.backButton)

        self.running = True
        while self.running:
            self.rend.enter_to_lobby()

            cursor_pos = pygame.mouse.get_pos()

            for button in buttons:
                button.check_cursor_hover(cursor_pos)

            self.rend.addressBox.check_cursor_hover(cursor_pos)

            # for event in pygame.event.get():
            #     self.rend.addressBox.handle_event(event)

            method = self.check_events()
            if method: return method



