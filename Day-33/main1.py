dic = {"name": "John", "age": 30, "city": "New York"}

print(dic["name"])
print(dic.get('age'))

print(dic.keys())
print(dic.values())
print(dic.items())

for key, value in dic.items():
    print(f"{key}: {value}")

print(dic.get('name1')) # Using get() method to avoid KeyError

print(dic["name1"]) # This will raise a KeyError if 'name1' does not exist