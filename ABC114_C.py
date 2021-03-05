# C - 755
N=int(input())

ans=0

def num753(num):
    global ans
    if num>N:
        return True
    if '7' in str(num) and '5' in str(num) and '3' in str(num):
        ans+=1
    nextnum1=num*10+3
    nextnum2=num*10+5
    nextnum3=num*10+7
    # print(nextnum1,nextnum2,nextnum3)
    num753(nextnum1)
    num753(nextnum2)
    num753(nextnum3)


num753(7)
num753(5)
num753(3)
print(ans)