import itertools
def Cal_Dist(i,j):
    a=((i[0]-j[0])**2+(i[1]-j[1])**2)**0.5
    return a

N=int(input())

town=[[0]*2 for i in range(N)]
for i in range (N):
    xy=list(map(int,input().split()))
    town[i]=xy
R=list(itertools.permutations(range(N)))

distance=[]


for k in range(len(R)):
    temp_town=[]
    for h in range(N):
        temp_town.append(town[R[k][h]])
    
    temp_distance=[]
    for i in range (N-1):
        distance_sections=Cal_Dist(temp_town[i],temp_town[i+1])
        temp_distance.append(distance_sections)
    else:
        distance.append(sum(temp_distance))
        # print(a,b,c,temp_distance)

# print(town)
# print(R)
print(sum(distance)/len(R))