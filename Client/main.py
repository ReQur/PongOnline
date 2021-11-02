from game import Game


def main():
    game = Game()

    Stage = game.main_menu

    while True:
        Stage = State()
        if Stage == None:
            break


if __name__ == "__main__":
    main()
