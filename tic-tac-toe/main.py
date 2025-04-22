from models import *
class TicTocToe:
    def __init__(self):
        self.player1 = Player('X', 'Shubham')
        self.player2 = Player('O','Rahul')
        self.board = Board()
        self.current_player = self.player1

    def switch_player(self):
        self.current_player = self.player1 if self.current_player== self.player2 else self.player2
    
    def start(self):
        while True:
            self.board.display()
            print(f'Current Player is {self.current_player.name}')
            r = int(input('Enter row number 0 to 2: '))
            c = int(input('Enter col number 0 to 2: '))
            while not self.board.move(self.current_player,r,c):
                print('OOPS! make sure enter valid and empty box')
                r = int(input('Enter row number 0 to 2: '))
                c = int(input('Enter col number 0 to 2: '))
            if self.board.check_win(self.current_player):
                print(f"Whoooo {self.current_player.name} wins!")
                break
            if self.board.is_full():
                print(f"OOOH the match is draw")
                break
            self.switch_player()

if __name__ == '__main__':
    TicTocToe().start()
    print("Have a nice day!")



        

