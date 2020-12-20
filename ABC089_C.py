import collections
import itertools

N=int(input())

ans=0

march=['M','A','R','C','H']
c=list(itertools.combinations(march,3))
names=collections.defaultdict(list)

ans=0

for i in range (N):
    s=input()
    names[s[0]].append(s)

for i in range(len(c)):
    ans+=len(names[c[i][0]])*len(names[c[i][1]])*len(names[c[i][2]])

# print(c)
# print(names)
print(ans)