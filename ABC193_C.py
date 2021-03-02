# キャディプログラミングコンテスト2021(AtCoder Beginner Contest 193)
# C - Unexpressed

# print(10**10)     # 10000000000
# print(2**34)      # 17179869184
# print(3**34)      # 16677181699666569
# print(4**34)      # 295147905179352825856
# N=10**10
N=int(input())

R=int(N**0.5)+1
Nums=set()

for i in range (2,R):
    for j in range (2,34):
        num=i**j
        if num<=N:
            Nums.add(num)
        else:
            break

print(N-len(Nums))