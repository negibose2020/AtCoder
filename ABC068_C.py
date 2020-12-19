from collections import defaultdict

N,M=map(int,input().split())

dic=defaultdict(list)

for i in range (M):
    a,b=map(int,input().split())
    dic[a].append(b)
    dic[b].append(a)

# line=len(dic[1])
line=dic[1]
if N in line:
    print("POSSIBLE")
    exit()
else:
    for i in range (len(line)):
        line2=dic[line[i]]
        if N in line2:
            print("POSSIBLE")
            exit()

print("IMPOSSIBLE")