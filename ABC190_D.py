# AtCoder Beginner Contest 190
# D - Staircase Sequences

N=int(input())

ans=0

for i in range (1,10**7):
    # 2*N=i*i+2*a*i-i
    # 2*a*i=2*N-(i*i)+i
    a=(2*N-(i*i)+i)/(2*i)
    if a<=0:
        print(ans*2)
        exit()
    if a==a//1:
        # print(i,a)
        ans+=1
    # if a==0:
    #     print(ans*2)
    #     exit()

print(ans)