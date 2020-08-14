# AtCoder Regular Contest 080
# C - 4-adjacent

N=int(input())
alist=list(map(int,input().split()))

oddcount=0
mod40=0
other=0

for a in alist:
    if a%2==1:
        oddcount+=1
    elif a%4==0:
        mod40+=1
    else:
        other+=1

if N==1:
    if mod40==N:
        print("Yes")
        exit()
    else:
        print("No")
        exit()
if N==2 or N==3:
    if mod40>0 or other==N:
        print("Yes")
        exit()
    else:
        print("No")
        exit()
# ↑ここまではあってそう。

if N%2==1:  # N>3 ,Nが奇数の時
    if (N-((other//2)*2))//2 <= mod40:
        print("Yes")
        exit()
    else:
        print("No")
        exit()

else:   # N>3 ,Nが偶数の時
    if other%2==1:  #かつ、要素が偶数である数が奇数の時  
        if (N-((other//2)*2))//2 <= mod40:
            print("Yes")
            exit()
        else:
            print("No")
            exit()
    else:
        if (N-((other//2)*2))//2 <= mod40:
            print("Yes")
            exit()
        else:
            print("No")
            exit()
