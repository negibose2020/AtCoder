# AtCoder Heuristic Contest 001
# A - AtCoder Ad

def Calculate_points(x1,y1,x2,y2,r,n):
    w=x2-x1
    h=y2-y1
    s=w*h
    p=1-(1-min(s,r)/max(s,r))**2
    p/=n
    return p

class Advertisement(object):
    def __init__(self,x,y,r,i):
        self.x=x
        self.y=y
        self.r=r
        self.dist_left=self.x-0
        self.dist_right=10000-self.x
        self.dist_up=self.y-0
        self.dist_down=10000-self.y
        self.num_i=i
    
    def update_dist_left(self,other):
        if self.x>other.x:
            self.dist_left=min(self.dist_left,self.x-other.x)
    def update_dist_right(self,other):
        if self.x<other.x:
            self.distt_right=min(self.dist_right,other.x-self.x)
    def update_dist_up(self,other):
        if self.y<other.y:
            self.dist_up=min(self.dist_up,other.y-self.y)
    def update_dist_down(self,other):
        if self.y>other.y:
            self.dist_down=min(self.dist_down,self.y-other.y)
    





n=int(input())
ads=[]
AdObjs=[]


for i in range (n):
    x,y,r=map(int,input().split())
    ads.append([x,y,r,i])
    obj=Advertisement(x,y,r,i)
    AdObjs.append(obj)


x0y0=Advertisement(0,0,0,n+100)
x10000y0=Advertisement(10000,0,0,n+101)
x0y10000=Advertisement(0,10000,0,n+102)
x10000y10000=Advertisement(10000,10000,0,n+103)

AdObjs.append(x0y0)
AdObjs.append(x10000y0)
AdObjs.append(x0y10000)
AdObjs.append(x10000y10000)

for i in range (n):
    a=AdObjs[i]
    for j in range (n+4):
        if i==j:
            pass
        b=AdObjs[j]
        if a.x-b.x>0 and a.y-b.y>0:
            Advertisement.update_dist_up(b,a)
            Advertisement.update_dist_left(b,a)
        if a.x-b.x>0 and a.y-b.y<=0:
            Advertisement.update_dist_left(b,a)
            Advertisement.update_dist_down(b,a)
        if a.x-b.x<=0 and a.y-
        Advertisement.update_dist_down(a,b)
        # Advertisement.update_dist_down(b,a)
        Advertisement.update_dist_left(a,b)
        # Advertisement.update_dist_left(b,a)
        Advertisement.update_dist_right(a,b)
        # Advertisement.update_dist_right(b,a)
        Advertisement.update_dist_up(a,b)
        # Advertisement.update_dist_up(b,a)

for i in range (n):
    pr=AdObjs[i]
    x1=pr.x-pr.dist_left
    y1=pr.y-pr.dist_up
    x2=pr.x+pr.dist_right
    y2=pr.y+pr.dist_down
    print(x1,y1,x2,y2)
