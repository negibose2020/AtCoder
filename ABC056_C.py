X=int(input())
ans=[0]
for i in range(1,10**9):
    temp=ans[-1]+i
    ans.append(temp)
    if temp>=X:
        print(i)
        exit()