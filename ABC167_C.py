def CanIGetEnoughSkills(SkillPoints,M,X):
    for _ in range(M):
        if SkillPoints[_]<X:
            return False
        else:
            pass
    return True


N,M,X=map(int,input().split())
books=[]
for n in range(N):
    array= list(map(int,input().split()))
    books.append(array)
# print(books)

BookCost=[]
GetSkillPoints=[]
for i in range (N):
    BookCost.append(int(books[i][0]))
    GetSkillPoints.append(books[i][1:])

temp_cost=10**9

#bit全探索

for Cart in range (2**len(GetSkillPoints)):
    TotalCost=0
    SkillPoints=[0]*M
    
    for book in range(len(GetSkillPoints)):
        if (Cart>>book)&1==0:
            continue
        TotalCost+= BookCost[book]
        for skillelement in range(M):
            SkillPoints[skillelement]+=GetSkillPoints[book][skillelement]

    # print(TotalCost,SkillPoints)
    if CanIGetEnoughSkills(SkillPoints,M,X)== True:
        temp_cost=min(temp_cost,TotalCost)

Answer=temp_cost
if Answer==10**9:
    Answer=-1
    
print(Answer)
