# AtCoder Regular Contest 109
# A - Hands

a,b,x,y=map(int,input().split())

if a==b:
    print(x)
    exit()

if a>b:
    if a-b==1:
        print(x)
        exit()

    if y<2*x:
        print(x+(a-b-1)*y)
    else:
        print(x+(a-b-1)*2*x)

else:
    if y<2*x:
        print(x+(b-a)*y)
    else:
        print(x+(b-a)*2*x)
