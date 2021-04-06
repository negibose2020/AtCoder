N,Q=map(int,input().split())

G=[[False for i in range (N)] for j in range (N)]
# print(G)

for _ in range (Q):
    q=list(map(int,input().split()))
    if q[0]==1:
        a=q[1]-1
        b=q[2]-1
        G[a][b]=True

    if q[0]==2:
        a=q[1]-1
        fback=[]
        for i in range (N):
            if G[i][a]==True:
                fback.append(i)
        for j in range (N):
            if j in fback:
                G[a][j]=True

    if q[0]==3:
        a=q[1]-1
        ff=set()
        for i in range (N):
            if G[a][i]==True:
                for j in range (N):
                    if G[i][j]==True and j!=a:
                        ff.add(j)
        for k in range (N):
            if k in ff:
                G[a][k]=True

for i in range (N):
    ans=[]
    li=G[i]
    for j in range (N):
        if G[i][j]==True:ans.append("Y")
        else:ans.append("N")
    print("".join(ans))
