# a = 15
# b = 3

# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)
# print("Integer Division:", a // b)
# print("Modulus:", a % b)
# print("Exponentiation:", a ** b)
# print("Floor of Division:", a // b)
# print("Ceiling of Division:", -(-a // b))
# print("Absolute Value of -a:", abs(-a))
# print("Round of Division:", round(a / b))
# print("Square Root of a:", a ** 0.5)
# print("Power of a to b:", pow(a, b))

# name = "Kartikey"
# _55 = " is learning Python."
# print(name + _55)


# name = "Kartikey"
# number = 55
# nuber1 = 5.5
# is_student = True

# print(type(name))
# print(type(number))
# print(type(nuber1))
# print(type(is_student))

# first_number = 3
# second_number = 5

# print("Sum of two numbers is:", first_number + second_number)

# a = int(input("Enter first number: "))
# print("You entered:", a)
# print("Type of a is:", type(a))

# first_number = int(input("Enter first number: "))
# second_number = int(input("Enter second number: "))

# print("Sum of two numbers is:", first_number + second_number)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print("The average of two numbers is:", (a + b) / 2)

# user_name = input("Enter your name: ")
# age = int(input("Enter your age: "))

# print("Hello", user_name + ", you are", age, "years old.")

# a =int(input("Enter first number: "))
# b =int(input("Enter second number: "))
# c = float(input("Enter third number: "))

# average = (float(a) + float(b) + c) / 3

# print("The average of three numbers is:", average)

# string = "45"
# number = int(string)
# float_number = float(string)
# print(type(number), number)
# print(type(float_number), float_number)
# print(type(string), string)

# x = 10 + 3 * 2 ** 2
# print(x)

# a = 7
# b = 3

# c = a
# a = b
# b = c

# print("a:", a)
# print("b:", b)

# a = float(input("Enter a number: "))

# integer_part = int(a)
# decimal_part = float(a - integer_part)
# print("Integer part:", integer_part)
# print("Decimal part:", decimal_part)

# age = int(input("Enter the age : "))

# if age < 13:
#     print("He is a child.")

# elif age > 13 and age < 18:
#     print("He is a teenegar.")

# elif age > 18:
#     print("He is a adult.")

# else:
#     print("you eneterd wrong thing,")

# user_name = input("Enter the username : ")
# password =  input("Enter the password : ")

# if (user_name == "admin") and (password == "pass"):
#     print("Welcome on the page.")

# else:
#     print("you enter wrong user_name or password.")

# color = input("enter the color : ")

# match color:
#     case "Green":
#         print("Go")
#     case "Yellow":
#         print("Stop")
#     case "Red":
#         print("Stop")
#     case _:
#         print("you entered wrong color")


# count = 1

# while count <= 5:
#     print("Count is:", count)
#     count += 1

# print("Loop ended. Count reached", count)

# n = int(input("Enter a number: "))

# i = 1

# while(i <= 10):
#     print(n, "*", i, "=", n * i)
#     i += 1

# i = 1

# while i <= 10:
#     print(i)
#     i += 2


# i = 1

# while i<= 10:
#     if i % 2 == 0:
#         i += 1
#         continue

#     print(i)
#     i += 1

# print("Loop ended.")

# string = "hello"

# for char in string:
#     print(char, end=",")


# string = "hello"

# char = input("Enter a character to search: ")

# if char in string:
#     print("Found")

# else:
#     print("Not Found")


# word = "artificial intelligence"

# count = 0

# for char in word:
#     if (char =='a') or (char == 'e') or (char == 'i') or (char == 'o') or (char == 'u'):
#         count += 1

# print("Number of vowels in the word is:", count) 

# def hello():
#     print("Hello, World!")

# hello()

# n = int(input("Enter a number: "))

# toPrint = 1
# for i in range(1,n+1):
#     for j in range(i):
#         print(toPrint, end=" ")
#         toPrint += 1
#     print()

# def average(a,b,c):
#     return (a+b+c)/3

# ans = average(5,10,15)
# print("The average is:", ans)

# sum = lambda a, b: a + b

# result = sum(5, 10)
# print("The sum is:", result)

# number = int(input("Enter a number: "))

# def factorial(n):
#     sum = 1
#     while n > 1:
#         sum = sum * n
#         n -= 1
#     return sum

# result = factorial(number)
# print("The factorial is:", result)

# n = int(input("Enter a Salary: "))

# if n < 0:
#     print("Invalid salary.")
# elif n < 30000:
#     print("your tax rate is 5%.")
# elif n <= 70000:
#     print("your tax rate is 15%.")
# else:
#     print("your tax rate is 25%.")

# def even_Number(a,b):
#     while a<=b:
#         if a%2==0:
#             print(a)
#         a+=1

# even_Number(3,15)

# x = print("Hello")
# print(x)

number = int(input("Enter a number: "))

def digit(n):
    while n > 0:
        digit = n % 10
        print(digit)
        n = n // 10

digit(number)


