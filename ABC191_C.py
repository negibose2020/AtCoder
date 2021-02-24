# AtCoder Beginner Contest 191
# C - Digital Graffiti

h,w=map(int,input().split())
area=[]
for _ in range (h):
    l=input()
    area.append(l)

ans=0

for i in range (h-1):
    for j in range (w-1):
        C=0
        if area[i][j]=="#":
            C+=1
        if area[i+1][j]=="#":
            C+=1
        if area[i][j+1]=="#":
            C+=1
        if area[i+1][j+1]=="#":
            C+=1
        if C==1 or C==3:
            ans+=1
print(ans)