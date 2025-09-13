def print_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

def check_winner(board, player):
    # Winning combinations (indices)
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # columns
        [0,4,8], [2,4,6]           # diagonals
    ]
    for combo in win_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def is_full(board):
    return " " not in board

def play_game():
    board = [" " for _ in range(9)]
    current_player = "X"

    while True:
        print_board(board)
        move = input(f"Player {current_player}, choose position (0-8): ")

        # validate input
        if not move.isdigit() or int(move) not in range(9):
            print("Invalid input. Choose number 0-8.")
            continue
        move = int(move)

        # check if spot empty
        if board[move] != " ":
            print("Spot already taken, try again.")
            continue

        # make move
        board[move] = current_player

        # check win
        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        # check draw
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # switch player
        current_player = "O" if current_player == "X" else "X"

# Run game
play_game()
