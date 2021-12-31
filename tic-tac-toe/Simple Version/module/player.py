import math
import random

class Player:
    def __init__ (self, symbol):
        self.symbol = symbol
    
    def get_move(self, turn):
        pass
    
class Computer(Player):
    def __init__ (self, symbol):
        super().__init__(symbol)
    
    def get_move(self, turn):
        pass

class Human(Player):
    def __init__ (self, symbol):
        super().__init__(symbol)
    
    def get_move(self, turn):
        pass