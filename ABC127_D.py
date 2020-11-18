import numpy as np


N,M=map(int,input().split())
# A=np.array(list(map(int,input().split())))
A=np.array(list(map(int,input().split())),dtype=np.int32)
A=np.sort(A)

EXC=[]

for i in range(M):
    exc=list(map(int,input().split()))
    EXC.append(exc)
excArry=np.array(EXC,dtype=np.int32)

col_num=1
Arr=excArry[np.argsort(excArry[:,col_num])[::-1]]
# print(A)
# print(Arr)

point=0


for j in range (M):
    change_Num=Arr[j][1]
    count=np.count_nonzero(A<change_Num)
    if count > 0:
        m=min(count,Arr[j][0])
        A[point:point+m]=change_Num
        point+=m
        # A=np.sort(A)
    else:
        break

print(np.sum(A))
    
#     for j in range (B):
#         count=np.count_nonzero(A<C)
#         if count>0:
#             m=min(B,count)
#             A[:m]=C
#         else:
#             continue
    
#     A=np.sort(A)

# print(np.sum(A))