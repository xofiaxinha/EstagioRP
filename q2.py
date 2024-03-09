def isFibonacci(n):
    a = 0
    b = 1
    while b < n:
        c = a + b
        a = b
        b = c
    return b == n

print(isFibonacci(13))