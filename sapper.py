import random 
class Cell:
    def __init__(self, mine = False, around_mines=0):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False
        
class GamePole:
    def __init__(self,N,M):
        self.N = N
        self.M = M
        self.pole = []
        self.init()
        
    def init(self):
        
        self.pole = [[Cell() for _ in range(self.N)] for _ in range(self.N)]
        cells = [(i,j) for i in range(self.N) for j in range(self.N)]
        random.shuffle(cells)
        for i,j in cells[:self.M]:
            self.pole[i][j].mine = True
        
        
        for i in range(self.N):
            for j in range(self.N):
                if not self.pole[i][j].mine:
                    count = 0
                for dx in (-1,0,1):
                    for dy in (-1,0,1):
                        if dx == 0 and dy == 0:
                            continue
                        x,y = i + dx, j + dy
                        if 0 <= x < self.N and 0 <= y < self.N:
                            if self.pole[x][y].mine:
                                count +=1
                self.pole[i][j].around_mines = count
                
                
    def show(self):
        for row in self.pole:
            for cell in row:
                if cell.fl_open:
                    print("*" if cell.mine else cell.around_mines, end = ' ')
                else:
                    print("#",end = ' ')
            print()
pole_game = GamePole(10,12)




