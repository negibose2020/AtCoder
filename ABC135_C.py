# ABC135
# C - City Savers
'''
町に残っているモンスター数の配列を用意する。
勇者iが倒せるのは町iと町i+1のモンスターだけ。
勇者i-1が町i(勇者iが担当)のモンスターを倒してくれているかもしれない。
町iのモンスターを倒して余力があれば町i+1のモンスターを倒しに行く。
さらに余力が残っていても、i+1番目の町までしか行けない。
モンスターが残っていない場合はあるが、モンスターの数が負の値になることはない。
倒した数を加算していき、答えとする。
'''

N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

count=0

D=[A[0]]

for i in range(N):
    s=B[i]-D[i]
    if s>0:
        d=A[i+1]-s
        if d>0:
            d=d
            count+=B[i]
        else :
            d=0
            count+=D[i]+A[i+1]
    else:
        d=A[i+1]
        count+=B[i]
    D.append(d)

print(count)