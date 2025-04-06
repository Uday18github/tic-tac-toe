import tkinter as tk
from tkinter import messagebox

def check_winner(board):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)  # Diagonals
    ]
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None

def on_click(index):
    global current_player, board
    if board[index] == " " and not check_winner(board):
        board[index] = current_player
        buttons[index].config(text=current_player)
        winner = check_winner(board)
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_board()
        elif " " not in board:
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"

def reset_board():
    global board, current_player
    board = [" " for _ in range(9)]
    current_player = "X"
    for button in buttons:
        button.config(text=" ")

# Initialize game state
board = [" " for _ in range(9)]
current_player = "X"

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create buttons
buttons = []
for i in range(9):
    button = tk.Button(root, text=" ", font=("Arial", 24), height=2, width=5,
                       command=lambda i=i: on_click(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Run the GUI event loop
root.mainloop()
