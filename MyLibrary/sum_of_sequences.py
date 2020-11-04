# 等差数列の和の公式
# デフォルトでは初項が1、公差が1として、項数を指定して使用。
def sum_of_arithmetic_sequences(n,a=1,d=1):
    S=n*(2*a+(n-1)*d)/2
    return S


# 等比数列の和の公式
# デフォルトでは初項が1、公比が2として、項数を指定して使用。
def sum_of_geometric_sequences(n,a=1,r=2):
    if r==1:
        return False
    S=a*(1-r**n)/(1-r)
    return S




print(sum_of_arithmetic_sequences(10))
print(sum_of_geometric_sequences(5,39,100))
