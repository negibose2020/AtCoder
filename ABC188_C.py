# AtCoder Beginner Contest 188
# C - ABC Tournament

def tournament(players):
    # 次の対戦に上がる参加者をリストで保持する。
    winners=[]

    # basecase
    if len(players)==2:
        if players[0][1]>players[1][1]:
            return players[1][0]
        else:
            return players[0][0]

    # else:
    # 対戦する各2名のうち、勝者をwinner配列に追加する。
    for i in range (len(players)//2):
        if players[i*2][1]>players[(i*2)+1][1]:
            winners.append([players[i*2][0],players[i*2][1]])
        else:
            winners.append([players[(i*2)+1][0],players[(i*2)+1][1]])
    
    return tournament(winners)


N=int(input())
A=list(map(int,input().split()))

ls=[]
# 参加者を[参加番号,強さ]の配列にして、リストに追加する。
for i in range (2**N):
    ls.append([i+1,A[i]])

ans=tournament(ls)

print(ans)
