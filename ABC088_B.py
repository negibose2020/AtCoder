N=int(input())
an=map(int,input().split())
Cards=[]
for a in an:
    Cards.append(int(a))
SortedCards=sorted(Cards,reverse=True)
AliceCards=SortedCards[0::2]
BobsCards=SortedCards[1::2]
print(sum(AliceCards)-sum(BobsCards))