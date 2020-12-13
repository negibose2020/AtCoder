# AtCoder Beginner Contest 083
# B - Some Sums
N,A,B=map(int,input().split())

ans=0
for i in range (1,N+1):
    # print(i)
    num=list(str(i))
    sumnum=0
    for j in range (len(num)):
        sumnum+=int(num[j])
    if A<=sumnum and sumnum<=B:
        # print(i)
        ans+=i

print(ans)