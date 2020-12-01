import collections

N,K=map(int,input().split())

ls=[]
for i in range (N):
    s=input()
    ls.append(s)

Col=collections.Counter(ls)
Com=Col.most_common()
# for a in Col:
    # print(a,Col[a])

# print(Col)
# print(Com[K-1])
if K==1 and len(Com)==1:
    print(Com[K-1][0])
    exit()

if K==1:
    if Com[K-1][1]==Com[K][1]:
        print("AMBIGUOUS")
    else:
        print(Com[K-1][0])

elif K==len(Com):
    if Com[K-1][1]==Com[K-2][1]:
        print("AMBIGUOUS")
    else:
        print(Com[K-1][0])

else:
    if Com[K-1][1]==Com[K-2][1]:
        print("AMBIGUOUS")
    elif Com[K-1][1]==Com[K][1]:
        print("AMBIGUOUS")
    else:
        print(Com[K-1][0])