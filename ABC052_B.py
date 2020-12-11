# AtCoder Beginner Contest 052
# B - Increment Decrement

N=int(input())
S=input()

num=0
ans=0

for i in range (N):
    if S[i]=="I":
        num+=1
    else:
        num-=1
    if num>ans:
        ans=num
print(ans)