# x = int(input("Enter a number: "))

# while x > 0:
#     print(x)
#     x = x-1

# x = 1

# while True:  # Infinite loop
#     print(x)  
#     x += 1

#     if x > 5:  # Condition to break the loop
#         break

while True:
    num = int(input("Enter a number greater than 10: "))
    
    if num > 10:
        print("Valid input received.")
        break  # Exit loop if condition is met
    
    print("Invalid input, try again!")