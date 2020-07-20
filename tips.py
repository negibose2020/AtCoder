# 素数のリスト作成

def is_prime(n):
    if n==1 or n==0:
        return False
    for k in range(2,int(n**0.5)+1):
        if n % k==0:
            return False
    else:
        return True


list_a=[x for x in range (10**5) if is_prime(x)==True]

print(list_a)