import numpy as np

N=int(input())
A=np.array(list(map(int,input().split())))

'''
以下、方針
・Aから、各要素の出現回数を取得する。
・出現回数から、組み合わせを計算する。
'''
unique_num, counts =np.unique(A,return_counts=True) #Aから、各要素の出現回数を取得する。

# print(unique_num)
# print(counts)
dic0={} #数字と出現回数の組合わせ辞書
dic1={} #数字と組合わせ個数の組合わせ辞書
dic2={} #回答用の辞書

Combination_pattern = []
for i in range(len(counts)):
    Combination = counts[i] * (counts[i]-1) // 2 #出現回数から、組み合わせを計算する。
    dic0[unique_num[i]]=counts[i]
    dic1[unique_num[i]]=Combination
    dic2.setdefault(unique_num[i])
    Combination_pattern.append(Combination)

totalcombination=sum(Combination_pattern)

# print(dic0)
# print(dic1)
# print(dic2)
# print(Combination_pattern)

'''
以下方針
・Aから数字を取得
・その数字の出現回数を1減らした状態の組み合わせの数を調べる。
・その数字に対応する元の組み合わせの数を減らし、1個前で計算した組合わせを足す。
・同じ数字を引いたときように答えを辞書に登録しておく。
・もし、過去に同じ数字を引いていたら、登録しておいた答えを回答する。
'''

for j in range (N):
    n=A[j] #Aから数字を取得
    if dic2[n]==None:
        reduced_pattern = (dic0[n]-1) * (dic0[n]-2) // 2 #その数字の出現回数を1減らした状態の組み合わせの数を調べる。
        ans=totalcombination-dic1[n]+reduced_pattern #その数字に対応する元の組み合わせの数を減らし、1個前で計算した組合わせを足す。
        dic2[n] = ans #同じ数字を引いたときように答えを辞書に登録しておく。
        print(ans)
    else:
        print(dic2[n]) #もし、過去に同じ数字を引いていたら、登録しておいた答えを回答する。