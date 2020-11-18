import numpy as np

N,M=map(int,input().split())
l=[]
for n in range(N):
    A,B=map(int,input().split())
    temp_l=[A,B]
    l.append(temp_l)
arr=np.array(l,dtype=np.int64) # dtypeでdataの型を指定しないとオーバーフロー
# print(l)
# print(arr)

need=M
ans=0


# numpyのarrayを、指定した要素番号の順番に並び替え。
# 今回の例では、金額(Ai)が安い順番に何本買えるかを調べるために、金額(Ai)を基準としてソート

col_num=0
route=arr[np.argsort(arr[:,col_num])]
# print(route)
for i in range(N):
    if need >= route[i,1]:
        ans+=route[i,0]*route[i,1]
        need-=route[i,1]
        if need==0:
            break
        else:
            continue
    else:
        ans+=route[i,0]*need
        need=0
print(ans)