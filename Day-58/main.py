class Details:
    def __init__(self, name, age):
        print("constructor is called")
        self.name = name
        self.age = age

    def info(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


obj1 = Details("Kartikey",20)
obj1.info()