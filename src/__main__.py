from DeepRL.opponent.RandomPlayer import RandomPlayer

def main() :
    player = RandomPlayer()
    print(player.makeAction("Choose a number between 1 and 3."))


if __name__ == '__main__' :
    main()