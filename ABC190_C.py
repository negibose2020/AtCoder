# AtCoder Beginner Contest 190
# C - Bowls and Dishes

N,M=map(int,input().split())

conditions=[]
for _ in range (M):
    a,b=map(int,input().split())
    conditions.append([a-1,b-1])

K=int(input())

playerselect=[]
for _ in range (K):
    c,d=map(int,input().split())
    playerselect.append((c-1,d-1))

ans=0

# bit全探索
for ptn in range(2**K):
    selection=[]
    dishes=[0]*N

    for player in range(K):
        if ptn>>player & 1 ==1:
            selection.append(1)
        else:
            selection.append(0)
    # print(selection)

    for select_i in range (K):
        Chosen_dish=playerselect[select_i][selection[select_i]]
        dishes[Chosen_dish] +=1
    
    tempans=0

    for condition_i in range (M):
        if dishes[conditions[condition_i][0]]>0 and dishes[conditions[condition_i][1]]>0:
            tempans+=1

    ans=max(ans,tempans)


print(ans)