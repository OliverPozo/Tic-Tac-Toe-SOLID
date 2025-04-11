from human_player import HumanPlayer
from game import Game

def main():
    player1 = HumanPlayer("Player 1", 'X')
    player2 = HumanPlayer("Player 2", 'O')

    game = Game(player1, player2)
    game.start()

if __name__ == "__main__":
    main()
