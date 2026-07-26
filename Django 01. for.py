lst = [2, 54, 78, 88, -54, -5, 54, 778, -56]
a = lst[0]
a *= 10
for i in range(len(lst)):
    lst[i] *= 10
    print(lst[i], end=' ')

print()

# for i in lst:
#     i *= 10
#     print(i, end=' ')
# print()
print(lst)
