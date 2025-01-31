tuple = (1,2,3,4,5,6,7, "Kartikey", "Mishra")

print(type(tuple))
print(type(tuple[3]))
print(len(tuple))
print(type(tuple[8]))


if "Kartikey" in tuple:
    print("Kartikey is present in the tuple")

else:
    print("Kartikey is not present in the tuple")