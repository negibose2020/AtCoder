# AtCoder Beginner Contest 081
# B - Shift only

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr


N=int(input())
A=list(map(int,input().split()))

ls=[]

for a in A:
    x=factorization(a)
    if x[0][0]!=2:
        print(0)
        exit()
    else:
        ls.append(x[0][1])
print(min(ls))