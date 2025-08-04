import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]): return True
        if all([board[j][i] == player for j in range(3)]): return True
    if all([board[i][i] == player for i in range(3)]): return True
    if all([board[i][2-i] == player for i in range(3)]): return True
    return False

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if not get_available_moves(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for move in get_available_moves(board):
            i, j = move
            board[i][j] = "O"
            score = minimax(board, depth + 1, False)
            board[i][j] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for move in get_available_moves(board):
            i, j = move
            board[i][j] = "X"
            score = minimax(board, depth + 1, True)
            board[i][j] = " "
            best_score = min(score, best_score)
        return best_score

def ai_move(board):
    best_score = -float("inf")
    best_move = None
    for move in get_available_moves(board):
        i, j = move
        board[i][j] = "O"
        score = minimax(board, 0, False)
        board[i][j] = " "
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe Game - You (X) vs AI (O)")
    print_board(board)

    while True:
        # Player move
        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter col (0, 1, 2): "))
            if board[row][col] != " ":
                print("Cell already taken. Try again.")
                continue
            board[row][col] = "X"
        except (ValueError, IndexError):
            print("Invalid input. Try again.")
            continue

        print_board(board)
        if check_winner(board, "X"):
            print("🎉 You win!")
            break
        if not get_available_moves(board):
            print("It's a draw!")
            break

        # AI move
        move = ai_move(board)
        if move:
            board[move[0]][move[1]] = "O"
            print("AI played:")
            print_board(board)
            if check_winner(board, "O"):
                print("AI wins! 😢")
                break

        if not get_available_moves(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
