import socket
import json
from threading import Thread


from player import Player
from point import Point

class Connection:
    ip = ""
    port = 3369
    sock = None
    server_addr = None
    this_client_player_side = None

    def __init__(self, ip):
        self.ip = ip
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_addr = (self.ip, self.port)
        self.sock.sendto(bytes('kek', encoding="utf-8"), self.server_addr)

    def close(self):
        self.sock.close()

    def recieve_data(self, playerLeft, playerRight, first_tick=False):
        data, _ = self.sock.recvfrom(1024)
        if len(data) > 10:
            dataDict = json.loads(data)[0]

            self.this_client_player_side = dataDict["playerSide"]

            point = Point(dataDict["Point"]["x"], dataDict["Point"]["y"], dataDict["Point"]["diameter"],
                          dataDict["Point"]["color"])

            playerLeft.x = dataDict["PlayerLeft"]["x"]
            if self.this_client_player_side != "left" or first_tick or dataDict["shouldReset"]:
                playerLeft.y = dataDict["PlayerLeft"]["y"]
            playerLeft.width = dataDict["PlayerLeft"]["width"]
            playerLeft.height = dataDict["PlayerLeft"]["height"]
            playerLeft.borderRadius = dataDict["PlayerLeft"]["borderRadius"]
            playerLeft.color = dataDict["PlayerLeft"]["color"]
            playerLeft.score = dataDict["PlayerLeft"]["score"]

            playerRight.x = dataDict["PlayerRight"]["x"]
            if self.this_client_player_side != "right" or first_tick or dataDict["shouldReset"]:
                playerRight.y = dataDict["PlayerRight"]["y"]
            playerRight.width = dataDict["PlayerRight"]["width"]
            playerRight.height = dataDict["PlayerRight"]["height"]
            playerRight.borderRadius = dataDict["PlayerRight"]["borderRadius"]
            playerRight.color = dataDict["PlayerRight"]["color"]
            playerRight.score = dataDict["PlayerRight"]["score"]

            return point, playerLeft, playerRight

    def send_data(self, playerLeft, playerRight):
        while True:
            Thread(target=lambda: self.sock.sendto(bytes(str(
                {
                    'left': playerLeft.y,
                    'right': playerRight.y
                }[self.this_client_player_side]), encoding="utf-8"), self.server_addr)).start()

