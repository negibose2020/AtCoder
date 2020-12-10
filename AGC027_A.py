# AtCoder Grand Contest 027
# A - Candy Distribution Again

import bisect

N,x=map(int,input().split())
a=list(map(int,input().split()))

a.sort()
a2=[0]
for i in range (N):
    a2.append(a2[-1]+a[i])

if x==sum(a):
    print(N)
    exit()

if x>sum(a):
    print(N-1)
    exit()

print(bisect.bisect(a2,x)-1)