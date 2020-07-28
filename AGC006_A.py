# AtCoder Grand Contest 006
# A - Prefix and Suffix

def f(word,N,S,T):
    if word[:N]==S and word[-N:]==T:
        return True
    else :
        return False

N=int(input())
S=input()
T=input()

ans = N*2

for i in range (N):
    t=T[N-i:]
    word=S+t

    if f(word,N,S,T):
        if ans>len(word):
            ans=len(word)
    else:
        pass

print(ans)