# AtCoder Beginner Contest 087
# C - Candies
'''
1列目のどこで下に下がるかを決める。
1列目で拾ったアメと、2列目で拾うアメの合計を記録していって最大値を出力
'''

N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

p=[]

for i in range (N):
    tempA=A[:1+i]
    tempB=B[0+i:]
    # print(tempA,tempB)
    p.append(sum(tempA)+sum(tempB))

print(max(p))