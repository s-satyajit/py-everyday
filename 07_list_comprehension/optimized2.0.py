thisislist = ["apple", "banana", "orange", "grapes", "pomegranade", "cherry"]
new_array = [x if x != "banana" else "orange" for x in thisislist]
print(new_array)