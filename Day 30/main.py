def factorial(num):
    if(num == 0 or num == 1):
        return 1
    else:
        return num * factorial(num - 1)
    
num = int(input("Enter a number: "))
print("Number is: ", num)
print("Factorial of", num, "is", factorial(num))