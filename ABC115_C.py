# AtCoder Beginner Contest 115
# C - Christmas Eve

N,K=map(int,input().split())

TREES=[]

for i in range (N):
    TREES.append(int(input()))
# print(TREES)

TREES.sort()
# print(TREES)

diff=[0]
for i in range (1,N):
    if i <K:
        d=abs(TREES[i]-TREES[0])
    else:
        d=abs(TREES[i]-TREES[i-K+1])
    diff.append(d)

# print(diff)
print(min(diff[K-1:]))