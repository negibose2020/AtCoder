N=int(input())
a=list(map(int,input().split()))

total=sum(a)

s=[0]
for i in range (N):
    s.append(s[-1]+a[i])

araiguma=[]
diff=[]
for i in range (N+1):
    araiguma.append(total-s[i])
    diff.append(abs(s[i]-araiguma[i]))

# print(araiguma)
# print(diff)
print(min(diff[1:-1]))