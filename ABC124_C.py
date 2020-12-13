# AtCoder Beginner Contest 124
# C - Coloring Colorfully

S=input()

start0=0
start1=0

for i in range(len(S)):
    n=int(S[i])
    if i%2==0:
        if n==0:
            pass
        else:
            start0+=1
    else:
        if n==0:
            start0+=1
        else:
            pass

for j in range(len(S)):
    n=int(S[j])
    if j%2==0:
        if n==1:
            pass
        else:
            start1+=1
    else:
        if n==1:
            start1+=1
        else:
            pass

print(min(start0,start1))