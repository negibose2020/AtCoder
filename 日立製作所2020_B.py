# 日立製作所 社会システム事業部 プログラミングコンテスト2020
# B - Nice Shopping

A,B,M=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

price=min(a)+min(b)
for i in range (M):
    x,y,c=map(int,input().split())
    if a[x-1]+b[y-1]-c<price:
        price=a[x-1]+b[y-1]-c

print(price)