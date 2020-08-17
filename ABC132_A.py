# AtCoder Beginner Contest 132
# A - Fifty-Fifty

S=input()

a=S[0]
b=S[1]
c=S[2]
d=S[3]
l=[a,b,c,d]
l.sort()

if l[0]==l[1] and l[2]==l[3] and l[1]!=l[2]:
    print("Yes")
else:
    print("No")