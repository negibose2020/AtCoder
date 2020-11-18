# AtCoder Regular Contest 105
# B - MAX-=min

import bisect
def f(arr):
    if arr[0]==arr[-1]:
        return arr[0]
    else:
        X=max(arr)
        x=min(arr)
        arr[-1]-=x
        arr=set(arr)
        arr=list(arr)
        arr.sort()
        print(arr)
        return f(arr)

N=int(input())
als=set(map(int,input().split()))
als=list(als)
als.sort()
# print(als)
hoge=f(als)

print(hoge)