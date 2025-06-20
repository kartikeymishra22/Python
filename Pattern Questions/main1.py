a = int(input("Enter a number: "))

for i in range(0, a):
    for j in range(0, a):
        print("*", end=" ")
    print()  # Move to the next line after printing a row of stars