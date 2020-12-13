# AtCoder Beginner Contest 113
# B - Palace

N=int(input())
T,A=map(int,input().split())
H=list(map(int,input().split()))

ans_diff=10**+7
ans_place=0

for i in range (N):
    t=T-H[i]*0.006
    if A<0 and t<0:
        diff=abs(t-A)
    elif A>=0 and t>=0:
        diff=abs(A-t)
    elif A<0 and t>=0:
        diff=t+abs(A)
    else:
        diff=A+abs(t)
    if diff<ans_diff:
        ans_diff=diff
        ans_place=i+1
print(ans_place)