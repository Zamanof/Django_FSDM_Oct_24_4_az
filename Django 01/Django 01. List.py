# list
# lst = []
# # lst1 = list()
# # print(type(lst))
# lst.append(5)
# lst.append(36)
# print(lst)
from ctypes import c_wchar

# list1 = [2, 54, 78, 88, -54, -5]
# list2 = list1 # shallow copy
# print(list1)
# print(list2)
# list2[0] = 25
# print()
# print(list1)
# print(list2)


# deep copy
# ver 1
# list3 = []
#
# for i in list1:
#     list3.append(i)
#
# print(list1)
# print(list3)
# list3[0] = 25
# print()
# print(list1)
# print(list3)

# # ver 2
# list4 = list1.copy()
#
# print(list1)
# print(list4)
# list4[0] = 25
# print()
# print(list1)
# print(list4)

# ver 3
# import copy
# list5 = copy.deepcopy(list1)
#
# print(list1)
# print(list5)
# list5[0] = 25
# print()
# print(list1)
# print(list5)

# ver 4
# list6 = list1[:]
#
# print(list1)
# print(list6)
# list6[0] = 25
# print()
# print(list1)
# print(list6)

# slice

lst = [2, 54, 78, 88, -54, -5, 54, 778, -56]
# print(lst[1:3])
# print(lst[1:7:2])
# print(lst[:3])
# print(lst[3:])
# print(lst[::2])
# print(lst[::-1])


# print(lst[-1])

print("Salam".find('b'))
