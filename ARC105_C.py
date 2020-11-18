# AtCoder Regular Contest 105
# 

def f(als):
    if len(als)==1:
        return als[0]
    else:
        arr=[als[0],]
        # print(als)
        for i in range (1,len(als)):
            # if als[i]>als[0]:
            # n=als[i]//als[0]
            arr.append(als[i]%als[0])
            arr=set(arr)
            arr=list(arr)
            arr.sort()
            # print(arr)
            if arr[0]==0:
                arr.pop(0)
    return f(arr)


    


N=int(input())
als=set(map(int,input().split()))
als=list(als)
als.sort()

hoge=f(als)
print(hoge)