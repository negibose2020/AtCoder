# AtCoder Grand Contest 019
# A - Ice Tea Store

def f(Q,H,S,D,N,M):
    QQ=Q
    QH=H/2
    QS=S/4
    QD=D/8

    if N==0:
        return M

    if N==1:
        if QQ==min(QQ,QH,QS):
            return M+(4*Q)

        if QH==min(QQ,QH,QS):
            return M+(2*H)
        
        if QS==min(QQ,QH,QS):
            return M+(S)
    else:
        if QQ==min(QQ,QH,QS,QD):
            return M+4*Q*N
            
        if QH==min(QQ,QH,QS,QD):
            return M+2*H*N
        
        if QS==min(QQ,QH,QS,QD):
            return M+S*N
        
        if QD==min(QQ,QH,QS,QD):
            if N%2==0:
                return M+(N//2)*D
            else:
                return f(Q,H,S,D,1,M+(N//2)*D)




Q,H,S,D=map(int,input().split())
N=int(input())

print(f(Q,H,S,D,N,0))