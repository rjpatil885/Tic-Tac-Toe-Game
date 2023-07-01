
class TicTacToe:
    def __init__(self):
        
        self.current_player = "X"  
        self.board = [["" for _ in range(3)] for _ in range(3)]  
        self.winner = None

    def make_move(self, row, col):

        if self.board[row][col] == "" and not self.winner:
            self.board[row][col] = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
            self.check_winner()

    def check_winner(self):

        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                self.winner = self.board[i][0]  
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                self.winner = self.board[0][i]  

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            self.winner = self.board[0][0] 
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            self.winner = self.board[0][2]  

    def check_draw(self):

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    return False 
        return True  