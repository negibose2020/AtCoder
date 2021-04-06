# AtCoder Beginner Contest 007
# C - 幅優先探索

import pprint
from collections import deque

R,C=map(int,input().split())
sy,sx=map(int,input().split())
gy,gx=map(int,input().split())

sy-=1
sx-=1
gy-=1
gx-=1

area=[]
for _ in range (R):
    area.append(input())

s=(sy,sx)
g=(gy,gx)

visited=[[-1 for i in range (C)] for j in range (R)]

q=deque()
q.append([sy,sx])
visited[sy][sx]=0

while len(q)>0:
    v=q.popleft()
    now=visited[v[0]][v[1]]
    # print(v)
    if [v[0],v[1]]==[gy,gx]:
        # print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        print(visited[v[0]][v[1]])
        # print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    if visited[v[0]-1][v[1]]==-1 and area[v[0]-1][v[1]]=='.' :
        q.append([v[0]-1,v[1]])
        visited[v[0]-1][v[1]]=now+1
    if visited[v[0]][v[1]-1]==-1 and area[v[0]][v[1]-1]=='.' :
        q.append([v[0],v[1]-1])
        visited[v[0]][v[1]-1]=now+1
    if visited[v[0]+1][v[1]]==-1 and area[v[0]+1][v[1]]=='.' :
        q.append([v[0]+1,v[1]])
        visited[v[0]+1][v[1]]=now+1
    if visited[v[0]][v[1]+1]==-1 and area[v[0]][v[1]+1]=='.' :
        q.append([v[0],v[1]+1])
        visited[v[0]][v[1]+1]=now+1
    # print(q)
    # print(area)
    # pprint.pprint(visited)
    # print("---------------------")

# print(area)

## BFS
## 幅優先探索