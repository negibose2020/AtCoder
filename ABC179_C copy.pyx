# AtCoder Beginner Contest 179
# C - A x B + C

cdef factorization(n):
    arr = []
    temp = n
    ans=1
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            # arr.append(cnt+1)
            ans*=(cnt+1)

    if temp!=1:
        # arr.append(1+1)
        ans*=2

    # if arr==[]:
        # arr.append(1+1)
        # ans*=2
    
    # arr=np.array(arr)

    # return np.prod(arr)
    return ans

N=int(input())
ans=0
for i in range (1,N):
    ans+=factorization(N-i)

print(ans)
# print(factorization(8))