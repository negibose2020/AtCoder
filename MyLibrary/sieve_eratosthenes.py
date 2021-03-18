# sieve_eratosthenes.py
# エラトステネスの篩

# 2～Nまでの素数の取得
def getPrimeNumbers(N):
    '''
    return primeNumbers from 2 to N
    '''
    prime_numbers=[]
    is_prime=[True]*(N+1)
    is_prime[0]=False
    is_prime[1]=False
    for i in range (2,N+1):
        if not is_prime[i]:
            continue
        prime_numbers.append(i)        
        for j in range (2*i,N+1,i):
            is_prime[j]=False
    return prime_numbers

# print(getPrimeNumbers(10**2))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def sieve_eratosthenes(N):
    '''
    return True/False list.
    ex is_prime[3]=True
    the number 3 is prime number
    '''
    is_prime=[True]*(N+1)
    is_prime[0]=False
    is_prime[1]=False
    for i in range (2,N+1):
        if not is_prime[i]:
            continue
        if i*i>=N:
            break
        for j in range (2*i,N+1,i):
            is_prime[j]=False
    return is_prime
# print(sieve_eratosthenes(25))