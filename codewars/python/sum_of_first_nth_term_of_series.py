# Code Wars - Sum of the first nth term of Series
def series_sum(n):
    numsum = 0
    for num in range(0,n):
        numsum += 1/(1+3*num)
    return str(format(numsum,".2f"))

n1 = 1
n2 = 2
n3 = 3
n5 = 5

# print(series_sum(n1))
# print(series_sum(n2))
# print(series_sum(n5))