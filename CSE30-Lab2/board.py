class Board:
        def __init__(self):
            # board is a list of cells that are represented 
            # by strings (" ", "O", and "X")
            # initially it is made of empty cells represented 
            # by " " strings
            a = ['a1','a2','a3']
            b = ['b1','b2','b3']
            c = ['c1','c2','c3']
            self.board = [a,b,c]
            # for i in 
            # self.sign = " "
            # self.size = 3
            # self.board = list(self.sign * self.size**2)
            # the winner's sign O or X
            self.winner = ""
        def get_size(self): 
            return self.size
             # optional, return the board size (an instance size)
        def get_winner(self):
            return self.sign
            # return the winner's sign O or X (an instance winner)     
        def set(self, cell, sign):
            pass
            # mark the cell on the board with the sign X or O
            # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
            # you can use a tuple ("A1", "B1",...) to obtain indexes 
            # this implementation is up to you 
        def isempty(self, cell):
            pass
              # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
            # return True if the cell is empty (not marked with X or O)
        def isdone(self):
            done = False
            self.winner = ''
            pass
            # check all game terminating conditions, if one of them is present, assign the var done to True
            # depending on conditions assign the instance var winner to O or X
            return done
        def show(self):
            pass
            # draw the board

if __name__=="__main__":
    b = Board()


