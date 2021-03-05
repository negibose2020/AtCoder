# A - 深さ優先探索
import sys
# import pprint
sys.setrecursionlimit(10000000)

def dfs(v):
    seen[v[0]][v[1]]=88
    # pprint.pprint(seen)
    if v==g:
        print('Yes')
        exit()
    if v[0]-1>=0 and area[v[0]-1][v[1]]!="#" and seen[v[0]-1][v[1]]==-1:
        u=[v[0]-1,v[1]]
        dfs(u)
        # seen[v[0]-1][v[1]]=True # seen[v[0]][v[1]]+1
        # todo.append([v[0]-1,v[1]])
    if v[0]+1<H and area[v[0]+1][v[1]]!="#" and seen[v[0]+1][v[1]]==-1:
        u=[v[0]+1,v[1]]
        dfs(u)
        # seen[v[0]+1][v[1]]=True # seen[v[0]][v[1]]+1
        # todo.append([v[0]+1,v[1]])
    if v[1]-1>=0 and area[v[0]][v[1]-1]!="#" and seen[v[0]][v[1]-1]==-1:
        u=[v[0],v[1]-1]
        dfs(u)
        # seen[v[0]][v[1]-1]=True # seen[v[0]][v[1]]+1
        # todo.append([v[0],v[1]-1])
    if v[1]+1<W and area[v[0]][v[1]+1]!="#" and seen[v[0]][v[1]+1]==-1:
        u=[v[0],v[1]+1]
        dfs(u)
        # seen[v[0]][v[1]+1]=True # seen[v[0]][v[1]]+1
        # todo.append([v[0],v[1]+1])


H,W=map(int,input().split())
area=[]
s=[0,0]
g=[1,1]
for i in range (H):
    c=input()
    if 's' in c: s=[i,c.index('s')]
    if 'g' in c: g=[i,c.index('g')]
    area.append(c)

seen=[]
for _ in range (H):
    seen.append([-1]*W)

dfs(s)

print('No')

# BFS
# 深さ優先探索