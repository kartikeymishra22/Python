# print("hello world")
# print(3)

# print("this does not " execute")
# print("this will\" execute")

# a = 1
# b = True
# c = "henry"
# d = None

# print(type(a))
# print((a))

import sys

a = 10
b = 123456789
c = "kartikey"
d = [1, 2, 3, 4]
e = (1, 2, 3)
f = {1, 2, 3}
g = {"a": 1, "b": 2}
h = True

print("int:", sys.getsizeof(a))
print("big int:", sys.getsizeof(b))
print("string:", sys.getsizeof(c))
print("list:", sys.getsizeof(d))
print("tuple:", sys.getsizeof(e))
print("set:", sys.getsizeof(f))
print("dict:", sys.getsizeof(g))
print("bool:", sys.getsizeof(h))
