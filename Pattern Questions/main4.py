a = int(input("Enter a number: "))

for i in range(1, a + 1):
    for j in range(1, i + 1):
        print(i, end=' ')
    print()  # Move to the next line after each row 
