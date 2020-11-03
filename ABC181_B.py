# AtCoder Beginner Contest 181
# B - Trapezoid Sum


N=int(input())

ans=0

for i in range (N):
    A,B=map(int,input().split())
    a=A*(A-1)//2
    b=B*(B+1)//2
    ans+=b-a

print(ans)