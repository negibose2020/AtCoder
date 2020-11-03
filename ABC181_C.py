# AtCoder Beginner Contest 181
# C - Collinearity

from itertools import combinations

def areTheseStraight(A,B,C):
    # a=(A[1]-B[1])/(A[0]-B[0])
    # aa=(B[1]-C[1])/(B[0]-C[0])

    if (A[1]-B[1])*(B[0]-C[0])==(B[1]-C[1])*(A[0]-B[0]):
        return True
    else:
        return False


N=int(input())

ls=[]

for i in range (N):
    xy=list(map(int,input().split()))
    ls.append(xy)

Combi=list(combinations(ls,3))

for i in range (len(Combi)):
    A=Combi[i][0]
    B=Combi[i][1]
    C=Combi[i][2]
    judge=areTheseStraight(A,B,C)
    if judge==True:
        print("Yes")
        exit()

print("No")