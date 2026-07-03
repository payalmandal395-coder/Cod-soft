import math

board = [' ' for _ in range(9)]

def print_board(b):
    print("\n")
    for i in range(0, 9, 3):
        print(f" {b[i]} | {b[i+1]} | {b[i+2]} ")
        if i < 6: print("-----------")
    print("\n")

def check_winner(b, player):
    win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(b[x] == b[y] == b[z] == player for x, y, z in win_conditions)

def is_full(b):
    return ' ' not in b

def minimax(b, depth, is_maximizing):
    if check_winner(b, 'O'): return 1
    if check_winner(b, 'X'): return -1
    if is_full(b): return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                score = minimax(b, depth + 1, False)
                b[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                score = minimax(b, depth + 1, True)
                b[i] = ' '
                best_score = min(score, best_score)
        return best_score

def get_best_move(b):
    best_score = -math.inf
    move = -1
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'O'
            score = minimax(b, 0, False)
            b[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move


# Refined Game Loop
print("--- Tic Tac toe:Human (X) vs AI (O) ---")
while not (is_full(board) or check_winner(board, 'X') or check_winner(board, 'O')):
    print_board(board)
    
    # Human Turn
    print("Game Starts :")
    try:
        user_move = int(input("Enter position (0-8): "))
        if board[user_move] == ' ':
            board[user_move] = 'X'
        else:
            print("Spot taken! Try again.")
            continue
    except (ValueError, IndexError):
        print("Invalid input! Please enter a number between 0 and 8.")
        continue

    # AI Turn
    if not (is_full(board) or check_winner(board, 'X')):
        print("AI is thinking...")
        ai_move = get_best_move(board)
        board[ai_move] = 'O'

# Final Result
print_board(board)
if check_winner(board, 'O'):
    print("AI wins!,Better luck next time.") 
elif check_winner(board, 'X'):
    print(" Congratulations,You win!")
else:
    print("It's a draw!")