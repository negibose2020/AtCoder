from collections import deque

n=int(input())
a=list(map(int,input().split()))

b=deque()
reverse=False
for i in range (n):
    if reverse==False:
        b.append(a[i])
        reverse=True
    else:
        b.appendleft(a[i])
        reverse=False
ans=[]
if reverse==False:
    for i in range (n):
        ans.append(b[i])
else:
    for i in range(n):
        ans.append(b.pop())


print(*ans)