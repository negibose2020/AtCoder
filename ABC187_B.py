# AtCoder Beginner Contest 187
# B - Gentle Pairs
class Coodinate (object):
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def lineSlope(self,other):
        deltax=self.x - other.x
        deltay=self.y - other.y
        slope=deltay/deltax
        if -1<=slope<=1:
            return True
        else:
            return False

N=int(input())
ls=[]

for _ in range (N):
    a,b =map(int,input().split())
    p=Coodinate(a,b)
    ls.append(p)

ans=0

for i in range (N):
    for j in range (i+1,N):
        if Coodinate.lineSlope(ls[i],ls[j]):
            ans+=1

print(ans)