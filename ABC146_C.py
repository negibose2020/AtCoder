def CanIBuy(A,B,mid):
    D=len(str(mid))
    price=A*mid+B*D
    return price

A,B,X=map(int,input().split())

left=0
right=10**9

for i in range(X):
    if left==right:
        if CanIBuy(A,B,(left+right)//2)<=X:
            print(left)
            exit()
        else:
            if left==0:
                print(0)
                exit()
            else:
                print(left-1)
                exit()
    else:
        pass
    
    if CanIBuy(A,B,(left+right)//2)<X:
        _left=left
        _right=right
        if left==(_left+_right)//2:
            left+=1
        else:
            left=(_left+_right)//2
    elif CanIBuy(A,B,(left+right)//2)>X:
        _left=left
        _right=right
        if right==(_left+_right)//2:
            right-=1
        else:
            right=(_left+_right)//2
    else:
        _left=left
        _right=right
        print((_left+_right)//2)
        exit()
