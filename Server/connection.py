import socket
import json
from threading import Thread


from player import Player
from point import Point

class Connection:
    port = 3369
    sock = None
    addrPlayerLeft = None
    addrPlayerRight = None
    recieve_thread_should_stop = False
    dataPlayerLeft = None
    dataPlayerRight = None

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('', self.port))

        _, self.addrPlayerLeft = self.sock.recvfrom(5)
        print(self.addrPlayerLeft)
        _, self.addrPlayerRight = self.sock.recvfrom(5)
        print(self.addrPlayerRight)


    def send_data(self, point, playerLeft, playerRight, playReflectSound=False, players_should_reset = False):
        leftPlayerDataList = [{
            "playerSide": "left",
            "shouldReset": players_should_reset,

            "Point": {
                "diameter": point.diameter,
                "x": point.x,
                "y": point.y,
                "color": point.color
            },
            "PlayerLeft": {
                "width": playerLeft.width,
                "height": playerLeft.height,
                "x": playerLeft.x,
                "y": playerLeft.y,
                "borderRadius": playerLeft.borderRadius,
                "color": playerLeft.color,
                "score": playerLeft.score
            },
            "PlayerRight": {
                "width": playerRight.width,
                "height": playerRight.height,
                "x": playerRight.x,
                "y": playerRight.y,
                "borderRadius": playerRight.borderRadius,
                "color": playerRight.color,
                "score": playerRight.score
            },
            "Sound": {
                "ReflectionSound": playReflectSound
            }
        }]

        rightPlayerDataList = [{
            "playerSide": "right",
            "shouldReset": players_should_reset,

            "Point": {
                "diameter": point.diameter,
                "x": point.x,
                "y": point.y,
                "color": point.color
            },
            "PlayerLeft": {
                "width": playerLeft.width,
                "height": playerLeft.height,
                "x": playerLeft.x,
                "y": playerLeft.y,
                "borderRadius": playerLeft.borderRadius,
                "color": playerLeft.color,
                "score": playerLeft.score
            },
            "PlayerRight": {
                "width": playerRight.width,
                "height": playerRight.height,
                "x": playerRight.x,
                "y": playerRight.y,
                "borderRadius": playerRight.borderRadius,
                "color": playerRight.color,
                "score": playerRight.score
            },
            "Sound": {
                "ReflectionSound": playReflectSound
            }
        }]

        thread1, thread2 = Thread(
            target=lambda: self.sock.sendto(bytes(json.dumps(leftPlayerDataList), encoding="utf-8"), self.addrPlayerLeft)), \
                           Thread(target=lambda: self.sock.sendto(bytes(json.dumps(rightPlayerDataList), encoding="utf-8"),
                                                             self.addrPlayerRight))
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()


    def recieve_data(self):
        while not self.recieve_thread_should_stop:
            data, addr = self.sock.recvfrom(5)
            if addr == self.addrPlayerLeft:
                self.dataPlayerLeft = data
            elif addr == self.addrPlayerRight:
                self.dataPlayerRight = data
