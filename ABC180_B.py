# AtCoder Beginner Contest 180
# B - Various distances

def ManhattanDistance(N,ls):
    ans=0
    for i in range (N):
        ans+=abs(ls[i])
    return ans

def EuclideanDistance(N,ls):
    ans=0
    for i in range (N):
        ans+=ls[i]*ls[i]
    return ans**0.5

def ChebyshevDistance(N,ls):
    ans=0
    for i in range (N):
        if abs(ls[i])>ans:
            ans=abs(ls[i])
    return ans


N=int(input())
xls=list(map(int,input().split()))

print(ManhattanDistance(N,xls))
print(EuclideanDistance(N,xls))
print(ChebyshevDistance(N,xls))