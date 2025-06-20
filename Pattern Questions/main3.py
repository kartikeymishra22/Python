a = int(input("Enter a number: "))

t0count = 1  # Initialize the counter variable

for i in range(1, a + 1):
    for j in range(1, a + 1):
        print(t0count, end=" ")
        t0count += 1
    print()  # Move to the next line after printing a row of numbers