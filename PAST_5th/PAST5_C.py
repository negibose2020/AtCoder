# 第五回 アルゴリズム実技検定
# C - 三十六進法


N=int(input())

d=[]
if N==0:
    print(0)
    exit()

while N>0:
    d.append(N%36)
    N=N//36

d=d[::-1]
ans=[]
num='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(len(d)):
    ans.append(num[d[i]])

print("".join(ans))