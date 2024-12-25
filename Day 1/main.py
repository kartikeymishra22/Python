# a = int(input("Enter the value of a : "))
# b = int(input("Enter the value of b : "))

# print(a+b)

# print("This does't " execute" ")
# print("This will \"execute\" ")

# Numeric Data
# a = 12
# b = 33.33
# c = (2 + 3j)

# print(type(a))
# print(type(b))
# print(type(c))

# Text Data : string data

# str = "Hello world"
# print(type(str))

# Boolean Data : True / False

# d = True
# e = False

# print(type(d))
# print(type(e))

# Sequenced Data : List and Tuple data types

# list1 = [4,5, ["apple, banana"]]
# print(type(list1))

# tupple = (("Hello world", "Goodbye world"), ("name", "Kartikey mishra"))

# print(type(tupple))

# mapped data : dictionary data types

# dict1 = {
#     "name" : "Kartikey",
#     "age" : 20,
#     "canvote" : True
# ,}

# print(type(dict1))

# Calculator 

# a = int(input("Enter the value of a : "))
# b = int(input("Enter the value of b : "))

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# name = "harry"
# print("Hello, "+ name)

# print('He said, "I want to eat an apple".')

# name = "He said, I want to eat an apple."
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[0])

# for character in name:
#     print(character)

# print(len(name))

# str1 = "     Silver Spoon               "
# print(str1.strip().split())

# str2 = "His name is Dan."
# print(str2.index("Dan"))
# print(str2.find("Dan"))
# print(str2.find("Danieal"))

# a = 7
# str = "15"

# sum = int(str)

# print(sum + a)

# a =int(input("Enter the value of a:"))
# print(a)

# name = "He is a good boy."

# for character in name:
#     print(character )

# str1 = "Harry"
# print(len(str1))

# alphabets = "AbcDE"

# for i in alphabets:
#     print(i)

# str1 = "Hello!!!!"

# print(str1.rstrip("!"))

# str1 = "      Silver Spoon           "

# print(str1.strip().replace("Sp", "M"))

# str1 = "Welcome to Jungle"

# print(str1.center(50,"."))
# print(str1.capitalize())

# apple = 100
# budget = 500

# if(apple<= budget):
#     print("Alexa, buy an apple.")

# else:
#     print("Alexa, you have no money to buy anything")

# num = int(input("Enter a nuumber : "))

# if(num<0):
#     print("Number is negative")

# elif(num==0):
#     print("Number is zero")

# else:
#     print("Number is positive")

x =int(input("Enter the value of X : "))

match x :
    case 0:
        print("Zero!")
    
    case 1:
        print("One!")

    case 4:
        print("four!")

    case _:
        print(x)
