# AtCoder Grand Contest 014
# A - Cookie Exchanges 

def f(A,B,C,n):
    if A%2==1 or B%2==1 or C%2==1:
        return [1,n]
    if A==B==C:
        return [0,-1]
    tempA=A
    tempB=B
    tempC=C
    A=tempB//2+tempC//2
    B=tempA//2+tempC//2
    C=tempA//2+tempB//2
    return [2,[A,B,C,n+1]]


A,B,C=map(int,input().split())

flg = True
n=0

while flg == True:
    a=f(A,B,C,n)
    if a[0]==0:
        flg=False
        print(-1)
        exit()
    if a[0]==1:
        flg=False
        print(n)
        exit()
    if a[0]==2:
        n+=1
        A,B,C=a[1][0], a[1][1] , a[1][2]
