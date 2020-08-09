# AtCoder Beginner Contest 085
# C - Otoshidama 

N,Y = map(int,input().split())

for x in range (N+1):
    for y in range (N-x+1):
        if 10*x + 5*y + (N-x-y)==Y//1000:
            print (x,y,N-x-y)
            exit()

print(-1,-1,-1)