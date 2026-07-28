# dictionary - class 'dict' (C++ - map, C# - Hashtable, Dictionary<T>)
# dct = {}
# dct = dict()
#
# print(type(dct))
tpl = (2, 5)
dct = {
    1: "Salam",
    2.5: 2.35,
    "key": "Value",
    False: 3659,
    tpl: 2
}

# print(dct[tpl])
# print(dct[(2, 5)])

# print(dct["key"])
# dct["key"] = 35
# dct[2] = 35
#
# print(dct.keys())
# print(dct.values())
# print(dct.items())

for i in dct.values():
    print(f"{i} ", end=" ")
print()

for i in dct.keys():
    print(f"{i}:{dct[i]} ", end="  ")
print()

for key, value in dct.items():
    print(f"{key}:{value} ", end="  ")
print()


# **kwargs -> dict
def some(**kwargs):
    print(type(kwargs))


some(Salam=1, hi=2, cpp=35)

