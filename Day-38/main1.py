a = input("Enter a value between 1 and 10: - > ")

if a == "quit":
   raise ValueError("You have chosen to quit the program.")

if not (1 <= int(a)<= 10) :
    raise ValueError("The value must be between 1 and 10.")

# else:
#     print("The value is within the range.")
#     print(f"The value is: {a}")
#     print("Thank you for entering a valid value.")