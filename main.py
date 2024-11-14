import random
from game import Connect4, GameState
game = Connect4()
print("Welcome to connect 4")
while game.state == GameState.PLAYER_1_TURN or game.state == GameState.PLAYER_2_TURN:
    game.printBoard()
    if game.state == GameState.PLAYER_1_TURN:
        print("Player 1 turn")
        user_input = int(str(input()))
        print(f"Player 1 picked column {user_input}")
        if game.makeMove(user_input) == 0:
            print("invalid move")

    elif game.state == GameState.PLAYER_2_TURN:
        print("Player 2 turn")
        move = random.randint(0,game.columns-1)
        print(f"Player 2 picked column {move}")
        if game.makeMove(move) == 0:
            print("invalid move")

game.printBoard()
if game.state == GameState.PLAYER_1_WINNER:
    print("Player 1 wins")

if game.state == GameState.PLAYER_2_WINNER:
    print("Player 2 wins")

if game.state == GameState.STALEMATE:
    print("stalemate")