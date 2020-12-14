# AtCoder Beginner Contest 185
# B - Smartphone Addiction

N,M,T=map(int,input().split())

now=N   # 現在のバッテリー残量
time=0  # 現在時刻

for i in range (M):
    a,b=map(int,input().split())
    now=now-(a-time)
    if now<=0:
        print("No")
        exit()
    now+=(b-a)
    if now>=N:
        now=N
    time=b
    # print(now,time)

now=now-(T-time)
if now<=0:
    print("No")
    exit()
print("Yes")