# def square(n):
#     '''This function returns the square of a number'''
#     return n**2

# n = int(input("Enter a number: "))
# print(f"The square of {n} is {square(n)}")
# print(square.__doc__)


def squre(n):
    '''This function returns the square of a number'''
    return n**2

n = int(input("Enter a number: "))
print(squre.__doc__)
print(f"The square of {n} is {squre(n)}")