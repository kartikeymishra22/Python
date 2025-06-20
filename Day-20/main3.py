# a = input("Enter a name : ")

# def name(a):
#     print("Hello " + a)

# name(a)

a = int(input("Enter a number: "))

def sum(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
    return sum

result = sum(a)
print(result)