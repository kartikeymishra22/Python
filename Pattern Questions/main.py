a = int(input("Enter a number: "))

for i in range(1, a+1):
    for j in range(1, a+1):
        print(j, end=" ")
    print()  # Move to the next line after printing a row of numbers