# Lambda expression
import random


# Non pure functions example
# have side effects
# def change_global_value():
#     global a
#     a = 25
#
# a = 35
#
#
# def return_random_result(a: int)-> int:
#     return a + random.randint(10, 99)



# print(f"before call function: a = {a}")
#
# change_global_value()
#
# print(f"after call function: a = {a}")

# print(return_random_result(5))

# Pure functions
# 1. Funksiyanın eyni arqumentlər üçün qaytardığı
# nəticələr həmişə eynidir
# (yəni lokal static dəyişənlərdən,
# qeyri-lokal dəyişənlərdən,
# dəyişdirilə bilən istinad (mutable reference)
# arqumentlərindən və ya giriş axınlarından (input streams)
# asılı olaraq dəyişmir;
# başqa sözlə, referensial şəffaflıq (referential transparency)
# təmin edilir).
# 2. Funksiyanın yan təsirləri (side effects) yoxdur
# (yəni qeyri-lokal dəyişənləri, dəyişdirilə bilən istinad arqumentlərini
# və ya giriş/çıxış axınlarını (input/output streams) dəyişdirmir).
# def add(a:int, b:int)->int:
#     return a + b
#
# print(add(2, 5))



def filter_negative(lst: list)->list:
    negative = []
    for i in lst:
        if i < 0:
            negative.append(i)
    return negative

def my_filter(lst: list, predicate)-> list:
    filtered = []
    for i in lst:
        if predicate(i):
            filtered.append(i)
    return filtered


def isNegative(value:int)-> bool:
    return value < 0


def isEven(value:int)-> bool:
    # return True if value % 2 == 0 and value != 0 else False
    return value % 2 == 0 and value != 0

lst = [12, -5, 0, 34, -18, 7, -42, 15, -9, 28,
           -1, 56, -33, 19, -27, 3, -14, 41, -50, 22,
           -8, 11, -36, 49, -2]
# first-class object
func = isNegative




# print(filter_negative(lst))
# print(my_filter(lst, isNegative))
# print(my_filter(lst, isEven))
# lambda expressions -> lambda params_list: return_data
"""
def isNegative(value:int)-> bool:
    return value < 0
    
            equal
lambda x: x < 0
"""
print(my_filter(lst, lambda x: x < 0))
print(my_filter(lst, lambda x: x %2 == 0 and x != 0))

f = lambda x: x < 0

print(type(f))
"""
lambda expressions:

C++     ->  [](x){ return x< 0;}
C#      ->  x => x < 0
JS      ->  (x)=> { return x< 0 }
Python  ->  lambda x: x < 0
"""

# closure, generators, decorators in Python