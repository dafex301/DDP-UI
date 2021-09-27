# Creating Dictionary
tuple_of_tuples = (
    ("Indonesia", "Jakarta"),
    ("Italy", "Rome"),
    ("Germany", "Berlin")
)

capitals = dict(tuple_of_tuples)
print(capitals)

list_of_tuples = [
    ("Indonesia", "Jakarta"),
    ("Italy", "Rome"),  
    ("Germany", "Berlin")
]

capitalz = dict(list_of_tuples)
print(capitalz)

print(capitalz["Indonesia"])
capitalz["Japan"] = "Tokyo"
print(capitalz)

print(len(capitalz))
cities = {"France": "Paris"}
capitalz.update(cities)
print(capitalz)

print(list(capitalz.values()))

for country in capitalz:
    print(country, "has capital", capitalz[country])

x = {}
for i in range(1,4):
    x[i] = i**3
print(x)