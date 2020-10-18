# AtCoder Beginner Contest 180
# D - Takahashi Unevolved


X,Y,A,B=map(int,input().split())

count=0

for i in range (100000):
    d=X*A
    if d<B:
        X=d
        count+=1
        if X>=Y:
            X=X//A
            count-=1
            break
    else:

        X+=B*((d-A)//B)
        count+=((d-A)//B)
        if X>=Y:
            X-=B*((d-A)//B)
            count-=((d-A)//B)
            break
for j in range (1000):
    count+=((Y-1)-X)//B
    X+=(((Y-1)-X)//B)*B
print(count)