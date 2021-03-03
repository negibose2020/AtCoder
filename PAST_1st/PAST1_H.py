def p(stock,evensell,oddsell):
    printingstock=[]
    for i in range (len(stock)):
        if i%2==0:
            printingstock.append(stock[i]-oddsell)
        else:
            printingstock.append(stock[i]-evensell)
    return printingstock


N=int(input())
stock=list(map(int,input().split()))
if N%2==0: n=N//2
else: n=(N//2)+1

om=stock[0]
em=stock[0]

ans=0
oddsell=0
evensell=0

for i in range (N):
    if i%2==0:
        om=min(om,stock[i])
    else:
        em=min(em,stock[i])


Q=int(input())

for i in range(Q):
    quelly=list(map(int,input().split()))
    if quelly[0]==1:
        a=quelly[1]-1
        b=quelly[2]
        if a%2==0:
            if stock[a]-oddsell>=b:
                ans+=b
                stock[a]-=b
                om=min(om,stock[a])
        else:
            if stock[a]-evensell>=b:
                ans+=b
                stock[a]-=b
                em=min(em,stock[a])

    if quelly[0]==2:
        a=quelly[1]
        if om-oddsell>=a:
            ans+=a*n
            oddsell+=a

    if quelly[0]==3:
        a=quelly[1]
        # print(om,oddsell,em,evensell)
        # print(a)
        # print(om-oddsell>=a,em-evensell>=a)
        if om-oddsell>=a and em-evensell>=a:
            ans+=a*N
            oddsell+=a
            evensell+=a
        else:
            pass
    # print(p(stock,evensell,oddsell))
print(ans)