# C - 隣接カウント

N,M=map(int,input().split())
area=["x"*(M+2)]
for i in range (N):
    _="x"
    s=input()
    _+=s
    _+="x"
    area.append(_)
area.append("x"*(M+2))
# print(area)

for i in range (1,N+1):
    ansls=""
    for j in range (1,M+1):
        ans=0
        for k in range (-1,2):
            for l in range (-1,2):
                # print(area[i+k][j+l])
                if area[i+k][j+l]=="#":
                    ans+=1
        ansls+=str(ans)
    print(ansls)