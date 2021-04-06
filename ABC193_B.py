# キャディプログラミングコンテスト2021(AtCoder Beginner Contest 193)
# B - Play Snuke

N=int(input())

ans=10**9+7

for i in range (N):
    a,p,x=map(int,input().split())
    if x-a>0:
        ans=min(ans,p)

if ans==10**9+7:
    ans=-1

print(ans)