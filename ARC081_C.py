import itertools
import collections

N=int(input())
A=list(map(int,input().split()))

C=collections.Counter(A)

clct=[]

for k,v in C.items():
    if v>=2:
        clct.append([k,v])

clct.sort()

if len(clct)<2:
    print(0)
    exit()

# print(clct)
w=clct.pop()
if w[1]>=4:
    print(w[0]*w[0])
    exit()
else:
    h=clct.pop()
    print(w[0]*h[0])
    exit()