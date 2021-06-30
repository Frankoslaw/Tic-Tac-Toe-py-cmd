class Board():
    def __init__(self):
        self.cells = [" "] * 9

    def display(self):
        for i in range(3):
            print(f'{self.cells[i * 3]} | {self.cells[i * 3 + 1]} | {self.cells[i * 3 + 2]}')
            if(i < 2):
                print('---------')

    def update_cell(self, num, player):
        if(self.cells[num - 1] == " "):
            self.cells[num - 1] = player
            return(1)
        return(0)

    def is_winner(self, player):
        for i in range(3):
            if(self.cells[i * 3] == player and self.cells[i * 3 + 1] == player and self.cells[i * 3 + 2] == player):
                return True
            if(self.cells[0 + i] == player and self.cells[3 + i] == player and self.cells[6 + i] == player):
                return True
        if(self.cells[0] == player and self.cells[4] == player and self.cells[8] == player):
            return True
        if(self.cells[2] == player and self.cells[4] == player and self.cells[6] == player):
            return True

    def is_tie(self):
        for cell in self.cells:
            if(cell == " "):
                return False
        return True

class Game():
    def __init__(self):
        self.board = Board()

        os.system("clear")
        print('Tic Tac Toe v0.1 made by Franciszek Łopuszański\n')

    def display_cmd( self ):
        os.system("clear")
        self.board.display()

    def make_move( self, player):
        while(1):
            os.system("clear")
            self.display_cmd()

            x_choice = int(input(f"Player: {player}, choose field from 1 - 9:"))
            if(self.board.update_cell(x_choice, player)):
                break

    def check_state( self ):
        for player in ["X", "O"]:
            if self.board.is_winner(player):
                os.system("clear")
                print(f"{player} wins")
                while(1):
                    cont = input("Press Y to continue")
                    if(cont == "Y"):
                        self.board.cells = [" "] * 9
                        return()
                    else:
                        exit(0)

        if self.board.is_tie():
            os.system("clear")
            print("Tie")
            cont = input("Press Y to continue")
            while(1):
                cont = input("Press Y to continue")
                if(cont == "Y"):
                    self.board.cells = [" "] * 9
                    return()
                else:
                    exit(0)
        
        return()

if __name__ == "__main__":
    import os
    game = Game()

    while(True):
        game.make_move("X")
        game.check_state()
        game.make_move("O")
        game.check_state()