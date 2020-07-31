# AtCoder Beginner Contest 135
# B - 0 or 1 Swap

'''
解説見て書き直し、
数列の要素と順番(i+1)が一致していない個数を数える。
これが3以上であれば"NO"
3未満(0か2)であれば"YES"
'''


N = int(input())
p = list(map(int,input().split()))

count = 0

for i in range (N) :
    if p[i] != i+1 :
        count += 1
    else :
        pass

if count < 3 :
    print('YES')
else :
    print('NO')