import json
import socket
from threading import Thread
from time import sleep, time_ns

from player import Player
from point import Point

from connection import Connection


def init():
    playerLeft = Player("LEFT", 0)
    playerRight = Player("NotLeft", 0)
    point = Point()

    players_should_reset = False
    playReflectSound = False

    result = {
        "Reflect": (True, False),
        "Reset": (False, True)
    }

    conn = Connection()

    conn.send_data(point, playerLeft, playerRight)

    recieve_thread = Thread(target=conn.recieve_data)
    recieve_thread.start()

    while conn.dataPlayerLeft == None or conn.dataPlayerRight == None:
        pass

    return point, playerLeft, playerRight, conn, result, recieve_thread, players_should_reset, playReflectSound


def data_update(conn, playerLeft, playerRight, recieve_thread):
    # 1) stop the recieve thread
    conn.recieve_thread_should_stop = True
    recieve_thread.join()

    # 2) save the client data in local scope
    leftPlayerData = conn.dataPlayerLeft
    rightPlayerData = conn.dataPlayerRight

    # 3) start the recieve thread
    conn.recieve_thread_should_stop = False
    recieve_thread = Thread(target=conn.recieve_data)
    recieve_thread.start()

    # 4) update the world state
    playerLeft.update_pos(int(float(leftPlayerData)))
    playerRight.update_pos(int(float(rightPlayerData)))

    return playerLeft, playerRight


def main():
    point, playerLeft, playerRight, conn, result, recieve_thread, players_should_reset, playReflectSound = init()


    while True:
        tick_start_ts = time_ns()

        playerLeft, playerRight = data_update(conn, playerLeft, playerRight, recieve_thread)

        if point.tick_calc(playerLeft, playerRight) == result["Reset"]:
            playerLeft = Player("LEFT", playerLeft.score + 1 if point.x > 400 else playerLeft.score)
            playerRight = Player("NotLeft", playerRight.score + 1 if point.x < 400 else playerRight.score)
            point = Point()
            players_should_reset = True

        elif point.tick_calc(playerLeft, playerRight) == result["Reflect"]:
            playReflectSound = True



        # 5) send the world state to clients
        conn.send_data(point, playerLeft, playerRight, playReflectSound, players_should_reset)

        playReflectSound = False
        players_should_reset = False

        seconds_taken = (time_ns() - tick_start_ts) / (10 ** 9)
        if seconds_taken < 1 / 50:
            sleep(1 / 50 - seconds_taken)


if __name__ == "__main__":
    main()
