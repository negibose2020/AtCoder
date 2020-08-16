# AtCoder Beginner Contest 175
# C - Walking Takahashi

X,K,D =map(int,input().split())

X=abs(X)

q=X//D
r=X%D

if K<=q:
    print(X-K*D)
    exit()

else :
    if (K-q)%2==0:
        print(r)
    else :
        print(abs(r-D))