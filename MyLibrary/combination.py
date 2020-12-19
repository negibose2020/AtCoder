import math
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
# base = comb(5,3)
# print(base) # 10