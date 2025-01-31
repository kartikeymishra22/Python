cities = {"Tokyo", "delhi", "Madrid", "Berlin"}
cities2 = {"Tokyo","Kabul","Seoul","delhi"}

# cities3 = cities.union(cities2)
# print(cities3)
# cities.update(cities2)
# print(cities)

cities3 = cities.difference(cities2)
print(cities3)
cities.difference_update(cities2)
print(cities)