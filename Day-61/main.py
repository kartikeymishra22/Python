class BaseClass:
    def __init__(self,name,id):
        self._name = name
        self._id = name

    def info(self):
        print(f"Name : {self._name} \nID : {self._id}")


class DerivedClass(BaseClass):
    def info(self):
        print("This is a derived class.")

obj = BaseClass('Kartik','123')
obj.info()  # Output: Name : Kartik  ID : 123

obj1 = DerivedClass('Kartik','123')
obj1.info()  # Output: This is a derived class.  # The info() method