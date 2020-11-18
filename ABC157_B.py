def IsBingo(arr_9):
    BINGO=['x','x','x']
    C1=arr_9[0::3]
    C2=arr_9[1::3]
    C3=arr_9[2::3]
    X1=[arr_9[0],arr_9[4],arr_9[8]]
    X2=[arr_9[2],arr_9[4],arr_9[6]]
    if (arr_9[:3]==BINGO or arr_9[3:6]==BINGO or arr_9[6:]==BINGO
     or C1==BINGO or C2==BINGO or C3==BINGO or X1==BINGO or X2==BINGO):
        return 'BINGO'


A1=list(input().split())
A2=list(input().split())
A3=list(input().split())
A=A1+A2+A3
N=int(input())
for _ in range(N):
    n=input()
    if A.count(n)==1:
        A[A.index(n)]="x"
# A1=A[:3]
# A2=A[3:6]
# A3=A[6:]
# print(A1,A2,A3)

if IsBingo(A)=='BINGO':
    print('Yes')
else:
    print('No')