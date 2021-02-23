# AtCoder Beginner Contest 189
# B - Alcoholic

N,X=map(int,input().split())
X*=100
al=0

for i in range (N):
    v,p=map(int,input().split())
    al+=v*p
    if al>X:
        print(i+1)
        exit()

print(-1)