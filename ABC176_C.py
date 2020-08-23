### This code is TLEcode ###


# AtCoder Beginner Contest 176
# C - Step

N=int(input())
Als=list(map(int,input().split()))

ans=0

for i in range (1,N):
    if Als[i]>=max(Als[0:i]):
        pass
    else :
        ans+= max(Als[0:i])-Als[i]
print(ans)