class Takahashi(object):
    def __init__(self):
        self.position_X=0
        self.position_Y=0
        self.command=[]
        self.yama=[]
    def move(self,targetCell_X,targetCell_Y):
        moveXNumber=targetCell_X-self.position_X
        moveYNumber=targetCell_Y-self.position_Y
        if moveXNumber<0:
            thisCommandX=["U"]*abs(moveXNumber)
            self.command.extend(thisCommandX)
        if moveXNumber>0:
            thisCommandX=["D"]*abs(moveXNumber)
            self.command.extend(thisCommandX)
        if moveYNumber<0:
            thisCommandY=["L"]*abs(moveYNumber)
            self.command.extend(thisCommandY)
        if moveYNumber>0:
            thisCommandY=["R"]*abs(moveYNumber)
            self.command.extend(thisCommandY)
        self.command.append("I")
        self.position_X=targetCell_X
        self.position_Y=targetCell_Y


    def allGet(self):
        for k in range (19):
            for i in range (20):
                # print(self.position_X)
                card=f.F[self.position_X][self.position_Y]
                if card>-1:
                    self.command.append("I")
                    self.yama.append(card)
                    f.noCard(self.position_X,self.position_Y)
                self.position_X+=1
                self.command.append("D")
            else:
                self.position_X-=1
                self.command.pop()
            self.position_Y+=1
            self.command.append("R")
            # print(self.position_X,self.position_Y)
            for j in range (20):
                if len(self.yama)==100:
                    break
                # print(self.position_X,self.position_Y)
                card=f.F[self.position_X][self.position_Y]
                if card>-1:
                    self.command.append("I")
                    self.yama.append(card)
                    f.noCard(self.position_X,self.position_Y)
                self.position_X-=1
                self.command.append("U")
            else:
                self.position_X+=1
                self.command.pop()

class F(object):
    def __init__(self):
        self.F=[[-1]*20 for i in range (20)]
    def cardput(self,x,y,num):
        self.F[x][y]=num
    def noCard(self,x,y):
        self.F[x][y]=-1

# main
takahashi=Takahashi()
f=F()

for i in range (70):
    x,y=map(int,input().split())
    takahashi.move(x,y)

for j in range (30):
    x,y=map(int,input().split())



print(str("".join(takahashi.command)))