import math
def sumOfSeries(n):
 
    sum = 0
    for i in range(1,n+1):
        sum = sum + (2 * i - 1) * (2 * i - 1)
    return sum
n= 10
print(sumOfSeries(n))
