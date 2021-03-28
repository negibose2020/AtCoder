# AtCoder Beginner Contest 194
# C - Squared Error

N=int(input())
A=list(map(int,input().split()))
accumA=[0]
for i in range (N):
    accumA.append(accumA[-1]+A[i])

ans=0

for i in range (N):
    num=A[i]
    temp=num*num
    temp*=(N-1)
    ans+=temp
    m=num*(accumA[-1]-accumA[i+1])
    ans-=2*m

print(ans)
