def fc(n):
    res = 1
    while n > 0:
        res = res * n
        n = n - 1
    return res
print(fc(5))