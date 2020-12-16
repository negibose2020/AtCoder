import numpy as np
import pprint

H,W=map(int,input().split())
e=[]
for i in range(H):
    a=list(input())
    for i in range (W):
        if a[i]=="#":
            e.append(a)
            break
    else:
        pass

col=[]

for i in range(len(e[0])):
    for j in range (len(e)):
        if e[j][i]=="#":
            break
        else:
            pass
    else:
        col.append(i)

col.reverse()
# print(col)
for i in range (len(col)):
    for j in range (len(e)):
        del e[j][col[i]]

for i in range (len(e)):
    print("".join(e[i]))
