# AtCoder Beginner Contest 180
# C - Cream puff

N=int(input())
ans=set()

for i in range (1,int(N**0.5)+1):
    if N%i==0:
        ans.add(i)
        ans.add(N//i)
ans=list(ans)
ans.sort()
for i in range (len(ans)):
    print(ans[i])
