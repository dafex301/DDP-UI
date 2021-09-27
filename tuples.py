# x = tuple("abc")
# print(x)

# y = tuple([2, 1, 2, 1])
# print(y)

# z = tuple(range(5))
# print(z)

# print(sum(z))

# for i in x:
#     print(i)

a = (5,7, 1)
b = (5,3,1)

x = 0
for i in range(len(a)):
    if a[i] == b[i]:
        x+=1
print(x)