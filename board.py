import tkinter as tk  
from tkinter import messagebox  
from game import TicTacToe 

class TicTacToeBoard:
    def __init__(self):
        self.game = TicTacToe() 
        self.root = tk.Tk() 
        self.root.title("Tic-Tac-Toe") 
        self.buttons = [[None for _ in range(3)] for _ in range(3)] 
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text="", width=10, height=5)
                self.buttons[i][j].configure(command=self.create_move_function(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def create_move_function(self, row, col):
        def make_move():
            self.make_move(row, col)
        return make_move

    def make_move(self, row, col):
   
        self.game.make_move(row, col)
        marker = self.game.board[row][col]
        self.buttons[row][col]["text"] = marker

        if self.game.winner:
            messagebox.showinfo("Game Over", f"Player {self.game.winner} wins!") 
            self.root.quit()
        elif self.game.check_draw():
            messagebox.showinfo("Game Over", "It's a draw!") 
            self.root.quit() 

    def start(self):
        self.root.mainloop()
