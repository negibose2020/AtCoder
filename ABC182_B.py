# AtCoder Beginner Contest 182
# B - Almost GCD

N=int(input())
Als=list(map(int,input().split()))

ansls=[0]*(max(Als)+1)

for i in range (N):
    for j in range (2,max(Als)+1):
        if Als[i]%j==0:
            ansls[j]+=1

maxG=max(ansls)

ans=ansls.index(maxG)
print(ans)




'''
N=int(input())
Als=list(map(int,input().split()))

ans=-1
kValue=-1

# for文のrangeに注意！2から開始。終了はmax(Als)なので、+1
for k in range (2,max(Als)+1):
    count=0
    for a in Als:
        if a%k==0:
            count+=1
    if count >ans:
        ans=count
        kValue=k

print(kValue)
'''



