class TicTacToe:
    def __init__(self):
        self.board = {
            "1": " ", "2": " ", "3": " ",
            "4": " ", "5": " ", "6": " ",
            "7": " ", "8": " ", "9": " "
        }
        self.current_winner = None
    
    def print_board(self):
        print(f"{self.board['1']} | {self.board['2']} | {self.board['3']}")
        print("---------")
        print(f"{self.board['4']} | {self.board['5']} | {self.board['6']}")
        print("---------")
        print(f"{self.board['7']} | {self.board['8']} | {self.board['9']}")
    