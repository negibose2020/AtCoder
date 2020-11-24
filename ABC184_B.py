# AtCoder Beginner Contest 184
# B - Quizzes

N,X=map(int,input().split())
S=input()


for i in range (N):
    if S[i]=="x":
        X=max(X-1,0)
    else:
        X+=1

print(X)