# HHKB プログラミングコンテスト 2020
# C - Neq Min

N=int(input())
Pls=list(map(int,input().split()))

mini=0
ansls=[0]*200003
for i in range(N):
    if Pls[i] > mini:
        ansls[Pls[i]]+=1
        print(mini)
    else:
        ansls[Pls[i]]+=1
        mini=ansls.index(0,mini)
        print(mini)