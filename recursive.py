def fc(n):
    res = 1
    while n > 0:
        res = res * n
        n = n - 1
    return res
#print(fc(5))

def fc2(n):
    # base case
    if n == 1:
        return 1;
    # recursion case
    else:
        return n * fc2(n-1)

print(fc2(10))