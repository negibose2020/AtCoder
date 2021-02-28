# キャディプログラミングコンテスト2021(AtCoder Beginner Contest 193)
# C - Unexpressed

def is_ok(num):
    '''
    okの条件を記載する。
    個別の問題でそれぞれ定義する。
    '''
    a=i**num
    if a<=n:
        return True
    else:
        return False

def megru_bisect(ok,ng):
    while(abs(ok-ng)>1):
        mid=(ok+ng)//2
        if is_ok(mid):
            ok=mid
        else:
            ng=mid
    return ok

# n=10**10
n=int(input())

R=int(n**0.5)+1
s=set()

ans=n
for i in range (2,R):
    y=megru_bisect(1,100)
    # ans-=y
    for j in range (2,y+1):
        s.add(i**j)
print(n-len(s))