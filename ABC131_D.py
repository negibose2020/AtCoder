# AtCoder Beginner Contest 131
# D - Megalomania

N=int(input())
ls=[]
for _ in range(N):
    p=list(map(int,input().split()))
    ls.append(p)

ls.sort(key= lambda x:x[1])
# print(ls)

time=0

for i in range (N):
    time+=ls[i][0]
    if ls[i][1] < time:
        print("No")
        exit()
    else:
        pass

print("Yes")