# AtCoder Beginner Contest 061
# B - Counting Roads

N,M=map(int,input().split())
R=[0]*(N+1)
for i in range (M):
    a,b=map(int,input().split())
    R[a]+=1
    R[b]+=1
for i in range (1,N+1):
    print(R[i])