# AtCoder Beginner Contest 168
# D - .. (Double Dots)
from collections import deque

N,M=map(int,input().split())
# 隣接リスト
# adjacencyList
G=[]
for _ in range (N):
    G.append([])
for _ in range (M):
    a,b=map(int,input().split())
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)

seen=[-1 for i in range (N)]
todo=deque()

seen[0]=0
todo.append(0)

while len(todo)>0:
    v=todo.popleft()
    for x in range (len(G[v])):
        y=G[v][x]
        if seen[y]==-1:
            seen[y]=v
            todo.append(y)
        else:
            continue
if sum(seen)==-1*N:
    print('No')
else:
    print("Yes")
    for i in range (1,N):
        print(seen[i]+1)

# print(seen)
# print(G)

# BFS
# 幅優先探索