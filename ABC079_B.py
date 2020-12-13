# AtCoder Beginner Contest 079
# B - Lucas Number

def Lucas(N):
    if L[N]>0:
        return L[N]
    if N==0:
        L[N]=2
        return 2
    if N==1:
        L[N]=1
        return 1
    L[N]=Lucas(N-2)+Lucas(N-1)
    return (Lucas(N-2)+Lucas(N-1))
L=[0]*100

print(Lucas(int(input())))