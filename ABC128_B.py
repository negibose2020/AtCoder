N=int(input())
l=[]
for i in range(N):
    S,P=map(str,input().split())
    b=' '
    if len(S)<10:
        S=S+b*(10-len(S))
    P=(100-int(P))
    l.append([S+str(P).zfill(3),i])
l.sort()

for i in range (N):
    print(l[i][1]+1)



# 先頭の桁を0で埋める。
# P='100'
# P4=P.zfill(4)
# print(P4)
# 基の数字の型がstrというのに注意