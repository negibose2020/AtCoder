# AtCoder Beginner Contest 042
# B - 文字列大好きいろはちゃんイージー

N,L=map(int,input().split())
arr=[]
for i in range (N):
    a=input()
    arr.append(a)
arr.sort()
print("".join(arr))