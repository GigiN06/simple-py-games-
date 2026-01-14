from config import *


class Grid:
    def __init__(self):
        self.gridmat=[]
        for i in range(9):
            row=[]
            for j in range(9):
                row.append(pygame.Rect(205+(40*i),70+(40*j),40,40))
            self.gridmat.append(row)
    def drawwhite(rect):
        pygame.draw.Rect(game.screen,'red',rect,3)

class Game:
    def __init__(self):
        self.mat=[[0 for _ in range(9)] for _ in range(9)]
        self.usermat=[[0 for _ in range(9)] for _ in range(9)]
        self.screen=pygame.display.set_mode((win_width,win_height))
        self.run=True
        self.scene=3
        self.clock=pygame.time.Clock()
        self.hour=0
        self.minute=0
        self.second=0
        self.startitemsinit()
        self.gameitemsinit()
    def startitemsinit(self):
        self.color1=(0,0,0)
        self.color2=(0,0,0)
        self.rect1=pygame.Rect(350,290,70,40)
        self.rect2=pygame.Rect(350,340,70,40)
        self.wait=pygame.time.get_ticks()
    def gameitemsinit(self):
        self.mat=genmat()
        self.grid=Grid()
        self.click=False
        self.x=self.y=0
        self.fixed=random.sample(list(itertools.product(range(10), repeat=2)), 19)
            
    def event(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.run=False
            if self.scene==2 and self.click==True:
                if event.type==pygame.KEYDOWN:
                    if event.unicode.isdigit():
                        self.usermat[self.x][self.y]=int(event.unicode)
                        self.click=False
            
    def update(self):
        self.event()
        self.mouse=pygame.mouse.get_pos()
        if self.scene==1:
            if self.rect1.collidepoint(self.mouse):
                self.color1=(255,255,255)
                if pygame.mouse.get_pressed()[0]:
                    self.mat=genmat()
                    self.wait=pygame.time.get_ticks()
                    self.scene=1.5
            else: self.color1=(0,0,0)
            if self.rect2.collidepoint(self.mouse):
                self.color2=(255,255,255)
                if pygame.mouse.get_pressed()[0]:
                     self.run=False
            else: self.color2=(0,0,0)
        if self.scene==1.5:
            if wait(self.wait,4000):
                self.mat=genmat()
                self.scene=2
        if self.scene==3.5:
            if wait(self.wait,300):
                self.scene=1
        if self.scene==3:
            if self.rect1.collidepoint(self.mouse):
                self.color1=(255,255,255)
                if pygame.mouse.get_pressed()[0]:
                    self.mat=genmat()
                    self.wait=pygame.time.get_ticks()
                    self.scene=3.5
                    self.wait=pygame.time.get_ticks()
            else: self.color1=(0,0,0)
        if self.scene==2:
            if self.usermat==self.mat:
                self.scene=3
                print("win")
            for i in range(9):
                for j in range(9):
                    if self.grid.gridmat[i][j].collidepoint(self.mouse):
                        if pygame.mouse.get_pressed()[0] and (i,j) not in self.fixed:
                            self.click=True
                            self.x=i
                            self.y=j                
    def draw(self):
        self.screen.fill((0,0,0))
        print(self.mat, self.usermat)
        if self.scene==1:
            displaytext(self.screen,"SUDOKU",90,'white',(win_width/2.6,150),255)
            pygame.draw.rect(self.screen,self.color1,self.rect1,3)
            pygame.draw.rect(self.screen,self.color2,self.rect2,3)
            displaytext(self.screen,"PLAY",40,'white',(win_width/2.2,300),255)
            displaytext(self.screen,"QUIT",40,'white',(win_width/2.2,350),255)
        if self.scene==1.5:
             displaytext(self.screen,"Generating a new board",60,'white',(win_width/4,150),255)
        if self.scene==2:
            for i in range(3):
                for j in range(3):
                    pygame.draw.rect(self.screen,'white',(205+(120*i),70+(120*j),120,120),3)  
            for i in range(9):
                for j in range(9):
                    pygame.draw.rect(self.screen,'white',self.grid.gridmat[i][j],1)
                    if (i,j) in self.fixed:
                        displaytext(self.screen,str(self.mat[i][j]),50,'white',(220+(i*40),80+(j*40)),255)
                        self.usermat[i][j]=self.mat[i][j]
                    if self.usermat[i][j]==0:
                        displaytext(self.screen,str(" "),50,'white',(220+(i*40),80+(j*40)),255)
                    else:
                        displaytext(self.screen,str(self.usermat[i][j]),50,'white',(220+(i*40),80+(j*40)),255)
            if self.click==True:
                pygame.draw.rect(self.screen,'red',self.grid.gridmat[self.x][self.y],5)
                self.usermat[self.x][self.y]=0
        if self.scene==3:
            displaytext(self.screen,"COMPLETED",90,'white',(win_width/2.9,150),255)
            pygame.draw.rect(self.screen,self.color1,self.rect1,3)
            displaytext(self.screen,"Menu",40,'white',(win_width/2.2,300),255)
            
        self.clock.tick(60)

    def main(self):
        self.update()
        self.draw()
        
        
        pygame.display.flip()
game=Game()
while game.run:
    game.main()
pygame.quit()
        