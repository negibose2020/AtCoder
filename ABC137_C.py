from collections import Counter

N=int(input())

dic={}
ans=0

for i in range(N):
    si=input()
    # ci=Counter(si)
    # c=sorted(ci.elements())
    # c=sorted(Counter(si).elements())
    sorted_s=''.join(sorted(Counter(si).elements()))
    if sorted_s in dic:
        ans+=dic[sorted_s]
        dic[sorted_s]+=1
    else:
        dic[sorted_s]=1

print(ans)


'''
dict 使用
配列操作よりも高速。
ハッシュテーブル使用している。
'''