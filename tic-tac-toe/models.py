class Player:
    def __init__(self, symbol,name):
        self.name = name
        self.symbol = symbol

class Board:
    def __init__(self):
        self.board = [['E']*3 for i in range(3)]

    def move(self,player, posx,posy):
        if posx>= 3 or posx<0 or posy>=3 or posy<0 or self.board[posx][posy] != 'E':
            return False
        self.board[posx][posy] = player.symbol
        return True

    def check_win(self, player):
        for i in range(3):
            if all([self.board[i][j]==player.symbol for j in range(3)]) or\
            all([self.board[j][i]==player.symbol for j in range(3)]):
                return True
        if all([self.board[i][i]==player.symbol for i in range(3)]) or\
        all([self.board[i][2-i]==player.symbol for i in range(3)]):
            return True
        return False
    
    def display(self):
        for i in range(3):
            for j in range(3):
                print(f"{self.board[i][j]} |",end=' ')
            print()
            print('-'*13)

    def is_full(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 'E':
                    return False
        return True


            
            
