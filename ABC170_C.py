X, N = map(int,input().split())
if N == 0:
    print(X)
    exit()

# titleの通り、使用を禁止された数字のリストが与えられる。
flist = list(map(int,input().split()))

if flist.count(X) == 0:
    print(X)
    exit()

# 使用禁止の数字を除いたリストを作るために、リストの素を作る。
l = list(range(0,102)) # ここの範囲設定が一番難しい部分だと思う。

# 使用を許可された数字のリストを作成する。
plist = []
for i in range(len(l)):
    if flist.count(l[i]) == 0:
        plist.append(l[i])

# Xを投入して、前後の数字との距離を計測していく。
plist.append(X)
anslist = sorted(plist)
t = anslist.index(X)

dist1 = anslist[t] - anslist[t-1] # Xと1つ前の数字との距離
dist2 = anslist[t+1] - anslist[t] # Xと1つ後ろの数字との距離
if dist1 <= dist2:
    print(anslist[t-1])
else:
    print(anslist[t+1])