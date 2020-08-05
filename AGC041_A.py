# AtCoder Grand Contest 041
# A - Table Tennis Training

def f(A,B,n) :
    judge=B-A

    if judge%2==0 :
        n+=judge//2
        return(n)

    else :
        if abs(A-1) < abs(N-B) :
            if A==1 :
                A=A
                B-=1
                n+=1
            else:
                B-=A-1
                n+=A-1
                A-=A-1
            return f(A,B,n)
        else :
            if B==N :
                B=B
                A+=1
                n+=1
            else :
                A+=abs(N-B)
                n+=abs(N-B)
                B+=abs(N-B)
            return f(A,B,n)

N,A,B=map(int,input().split())
print(f(A,B,0))


# import random
# for i in range (20):
#     A=random.randint(1,10**16)
#     B=random.randint(A,10**17)
#     N=random.randint(B,10**18)
#     print(f(A,B,0))
