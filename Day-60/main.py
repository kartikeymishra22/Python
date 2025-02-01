class MyClass:
    def __init__ (self, value):
        self._value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_val):
        self._value = new_val

    # def info(self):
    #     print(f"Value obj is {self.value}")


obj = MyClass(10)
obj.value = 20
print(f"New value of the obj is {obj.value}")
