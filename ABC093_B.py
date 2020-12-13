# AtCoder Beginner Contest 093
# B - Small and Large Integers

A,B,K=map(int,input().split())
S=set()
for i in range (A,A+K):
    if A<=i and i<=B:
        S.add(i)

for i in range (B-K+1,B+1):
    if A<=i and i<=B:
        S.add(i)
ls=list(S)
ls.sort()

for i in range (len(ls)):
    print(ls[i])