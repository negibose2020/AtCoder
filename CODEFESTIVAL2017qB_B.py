import collections
import bisect
N=int(input())
D=list(map(int,input().split()))
M=int(input())
T=list(map(int,input().split()))

D.sort()
T.sort()

DC=collections.Counter(D).most_common()
TC=collections.Counter(T).most_common()

# print(DC)
# print(TC)

for i in range(len(TC)):
    l=bisect.bisect_left(D,TC[i][0])
    r=bisect.bisect_right(D,TC[i][0])
    # print(TC[i][1],r-l)
    if D[l]==TC[i][0] and TC[i][1]<=r-l:
        pass
    else:
        print("NO")
        exit()

print("YES")