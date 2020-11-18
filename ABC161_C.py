N, K = map(int,input().split())

D1 = N//K
D2 = N//K+1

Ans = min(abs(N-D1*K) ,abs(N-D2*K))
print(Ans)