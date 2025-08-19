my_tuple = ("apple", "banana", "orange", "grapes", "pomegranade", "cherry")
another_tuple = ("element1",)
my_tuple+=another_tuple
print(my_tuple)

y = list(my_tuple)
y.append("element2")
my_tuple = tuple(y)
print(my_tuple)