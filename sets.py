# s1 = set("text")
# print(s1)

s1 = {5,2,3,1, 5, 2}
s2 = {1,10}
# print(s1)
# s1.add(4)
# print(s1)
# s1.remove(5)
# print(s1)
# s1.update({6,8})
# print(s1)

# # intersection
# print(s1 & s2)
# # union
# print(s1 | s2)
# # difference
# print(s1 - s2)

# print((s1 - s2) | (s2-s1))
# # symmetric difference
# print(s1 ^ s2)

# # subset/superset
# s1 = {1,2}
# s2 = {1,2,3}
# s3 = {3,4}

# print(s1<=s2)
# print(s2>s1)
# print(s1<s1)

# unique words
text = "a car a man a man"
print(text.split())
unique_text = set(text.split())
print(unique_text)

