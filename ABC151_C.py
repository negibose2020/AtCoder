N,M=map(int,input().split())
L1=[0]*(N+1) #正解判定、iは問題分中と一致
L2=[0]*(N+1) #WAのカウント用、iは問題分中と一致

for i in range(M):
    p,S=input().split()
    if L1[int(p)]==1:
        pass
    else:
        if S=='AC':
            L1[int(p)]=1
        else:
            L2[int(p)]+=1

for j in range (N+1):
    if L1[j]==0 and L2[j]>0:
        L2[j]=0

print(sum(L1),sum(L2))