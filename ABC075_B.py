# AtCoder Beginner Contest 075
# B - Minesweeper

def f(i,j):
    ans[i+1][j+1]+=10**9+7
    ans[i][j]+=1
    ans[i][j+1]+=1
    ans[i][j+2]+=1
    ans[i+1][j]+=1
    # ans[i+1][j+1]+=1
    ans[i+1][j+2]+=1
    ans[i+2][j]+=1
    ans[i+2][j+1]+=1
    ans[i+2][j+2]+=1


H,W=map(int,input().split())

ans=[[0]*(W+2) for i in range (H+2)]

area=[]
for i in range (H):
    area.append(input())

for i in range(H):
    for j in range (W):
        if area[i][j]=="#":
            f(i,j)


for i in range (H):
    A=ans[1+i][1:-1]
    for j in range (len(A)):
        if A[j]>10**9:
            A[j]="#"
        else:
            A[j]=str(A[j])
    print("".join(A))