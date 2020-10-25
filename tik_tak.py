import os 
class game:
    def __init__(self,player1,player2):
        self.player1=player1
        self.player2=player2
        self.arr=[[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        
        print('{}: X, {}: O'.format(self.player1,self.player2))      

    def board(self):
        for i in self.arr:
            for j in i:
                print('| {} |'.format(j),end=' ')
            print()
        print()

    def player1_move(self,number):
        for i in range(3):
            for j in range(3):
                if number == self.arr[i][j]:
                    self.arr[i][j] = 'X'
                    break

    def player2_move(self,number):
        for i in range(3):
            for j in range(3):
                if number == self.arr[i][j]:
                    self.arr[i][j] = 'O'
                    break

    def win(self):
        #vERTICAL WINS
        if self.arr[0][0] == 'X' and self.arr[1][0] == 'X' and self.arr[2][0] == 'X':
            return True
        elif self.arr[0][1] == 'X' and self.arr[1][1] == 'X' and self.arr[2][1] == 'X':
            return True
        elif self.arr[0][2] == 'X' and self.arr[1][2] == 'X' and self.arr[2][2] == 'X':
            return True
            
        elif self.arr[0][0] == 'O' and self.arr[1][0] == 'O' and self.arr[2][0] == 'O':
            return True
        elif self.arr[0][1] == 'O' and self.arr[1][1] == 'O' and self.arr[2][1] == 'O':
            return True
        elif self.arr[0][2] == 'O' and self.arr[1][2] == 'O' and self.arr[2][2] == 'O':
            return True
            
        #HORIZONTAL WINS
        elif self.arr[0][0] == 'X' and self.arr[0][1] == 'X' and self.arr[0][2] == 'X':
            return True
        elif self.arr[1][0] == 'X' and self.arr[1][1] == 'X' and self.arr[1][2] == 'X':
            return True
        elif self.arr[2][0] == 'X' and self.arr[2][1] == 'X' and self.arr[2][2] == 'X':
            return True
            
        elif self.arr[0][0] == 'O' and self.arr[0][1] == 'O' and self.arr[0][2] == 'O':
            return True
        elif self.arr[1][0] == 'O' and self.arr[1][1] == 'O' and self.arr[1][2] == 'O':
            return True
        elif self.arr[2][0] == 'O' and self.arr[2][1] == 'O' and self.arr[2][2] == 'O':
            return True

        #DIAGONAL WINS
        elif self.arr[0][0] == 'X' and self.arr[1][1] == 'X' and self.arr[2][2] == 'X':
            return True
        elif self.arr[0][2] == 'X' and self.arr[1][1] == 'X' and self.arr[2][0] == 'X':
            return True
            
        elif self.arr[0][0] == 'O' and self.arr[1][1] == 'O' and self.arr[2][2] == 'O':
            return True
        elif self.arr[0][2] == 'O' and self.arr[1][1] == 'O' and self.arr[2][0] == 'O':
            return True
        else:
            return False

    def draw(self):
        if self.arr[0][0]!=1 and self.arr[0][1]!=2 and self.arr[0][2]!=3 and self.arr[1][0]!=4 and self.arr[1][1]!=5 and self.arr[1][2]!=6 and self.arr[2][0]!=7 and self.arr[2][1]!=8 and self.arr[2][1]!=9:
            return True
        else:
            return False

    def play(self):
        self.board()
        count=0
        win1 = False
        win2 = False
        draw =False
        while not win1 and not win2 and not draw:
            if count % 2 == 0:
                number=int(input('{}: '.format(self.player1)))
                self.player1_move(number)
                os.system('cls')
                self.board()
                win1 = self.win()
                draw = self.draw()
            else:
                number=int(input('{}: '.format(self.player2)))
                self.player2_move(number)
                os.system('cls')
                self.board()
                win2 = self.win()
                draw = self.draw()
            count+=1
            
        if win1 == True:
            print('{} won the game'.format(self.player1))
        elif win2 == True:
            print('{} won the game'.format(self.player2))
        else:
            print('Draw')
if __name__ == '__main__':
    print('welcome to the game')
    o = 'y'
    first = 1
    play = 1
    k = 'y'
    while play == 1:
        if first == 0:
            o = input('play again: y or n ')
            if o == 'n':
                play = 0
            elif o == 'y':
                k = input('do you want to change players name: y or n ')
                if k == 'y':
                    p1 = input('player1 enter your name: ')
                    p2 = input('player2 enter your name: ')
                    game1=game(p1,p2)
                    game1.play()
                elif k == 'n':
                    game1=game(p1,p2)
                    game1.play()
        else:
            p1 = input('player1 enter your name: ')
            p2 = input('player2 enter your name: ')
            game1=game(p1,p2)
            game1.play()
            first = 0
            
