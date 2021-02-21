# SOMPO HD プログラミングコンテスト2021(AtCoder Beginner Contest 192)
# C - Kaprekar Number

def func(strNum):
    numlist=list(map(int,strNum))
    g1list=sorted(numlist,reverse=True)
    g2list=sorted(numlist)
    g1=int("".join(list(map(str,g1list))))
    g2=int("".join(list(map(str,g2list))))
    fx=g1-g2
    return fx

N,K=map(int,input().split())

n=N

for _ in range (K):
    n=func(str(n))

print(n)