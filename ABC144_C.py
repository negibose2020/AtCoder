
#素因数分解
def prime_factorization(N):
    n=N
    a=2
    prime_factor=[]
    while a**2<=n:
        while n%a==0:
            prime_factor.append(a)
            n//=a
        a+=1
    if n>1:
        prime_factor.append(n)
    return prime_factor


# N=50
N=int(input())

a=1
b=N//a
dis=abs(b-a)

for i in range(1,int(N**0.5)+1):
    if N%i==0:
        _a=i
        _b=N//i
        _dis=abs(_b-_a)
        if _dis<dis:
            a=_a
            b=_b
            dis=_dis

print(a-1+b-1)