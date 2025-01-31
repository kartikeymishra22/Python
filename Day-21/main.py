x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

z = input("What is the operation you want to perform?: ")

def calculate(x,y,z):
    match z:
        case '+':
            return x + y
        
        case '-':
             return x - y
        
        case  '*':
            return x * y
        
        case  '/':
            return x/y
        
        case  '%':
            return x%y
        
        case '**':
            return x**y
        
        case '//':
            return x//y
        
        case _:
            return "Invalid operation"
        
result = calculate(x, y,z)
print(result)
