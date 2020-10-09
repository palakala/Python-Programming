def findMissingNumber(a, n):
    x1, x2 = 0,0
    for i in range(1, n+1):
        x1 += i

    for i in range(n-1):
        x2 = x2 + a[i]
    return x1-x2

a = [1, 2, 3, 4, 6, 5, 8, 9, 10]
n = 10
print(findMissingNumber(a, n))
