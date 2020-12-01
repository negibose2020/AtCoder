# AtCoder Regular Contest 109
# B - log

n=int(input())

x=int((1+(8*n+9)**0.5)//2)

if x*(x+1)<=2*n+2:  # xまでの丸太を切り出せる
    print(n+1-x)
    exit()
if x*(x-1)<=2*n+2:  # x-1までの丸太を切り出せる
    print(n+1-x+1)
    exit()
else:
    print(n+1-x+2)  # x-2までの丸太を切り出せる(計算誤差で、あり得ることが何となくわかった)