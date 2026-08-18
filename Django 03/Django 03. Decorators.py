# Decorator
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Before")
        print(args)
        print(kwargs)
        result = original_function(*args, **kwargs)
        print(f"Function result: {result}")
        print("After")
        return result
    return wrapper_function


# @decorator_function
# def my_function(numb1, numb2):
#     return numb1 + numb2
#
#
# @decorator_function
# def other_function(numb1, numb2, numb3):
#     return numb1 * numb2 - numb3
#
# print(my_function(25, 26))
# print()
# print(other_function(25, 26, 50))

# authorize check example
def is_authenticate(login, password):
    return login == "admin" and password == "admin"


def checkAuthenticate(func):
    def wrapper(*args, **kwargs):
        if is_authenticate(kwargs["login"], kwargs["password"]):
            print("User authenticated")
            return func(*args, **kwargs)
        else:
            raise Exception("User unauthenticate")
    return wrapper

@checkAuthenticate
def do_something(login:str, password:str):
    print("Do something")

# do_something(login="admin", password="admin")

# validate example
def validate_arguments(func):
    def wrapper(*args, **kwargs):
        for arg in [*args, *kwargs.values()]:
            if not isinstance(arg, int):
                raise TypeError(f"Argument must be an integer: {arg}")
        return func(*args, **kwargs)
    return wrapper


@validate_arguments
def summ(left:int, right:int)->int:
    return left + right

@validate_arguments
def my_range(start:int, stop:int=None, step:int=1)-> list:
    lst = []
    if stop is None:
        stop = start
        start = 0
    while start < stop:
        lst.append(start)
        start += step
    return lst


print(summ(25, 2))
print(summ(left=25, right=265))
# print(summ(left="25", right=265))

print(my_range(start=10, stop=20, step=2))

