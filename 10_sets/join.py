set1 = {"a", "b", "c", "d"}
set2 = {1, 2, 3, 4, 5, "a"}
set3 = {"john", "ellina"}
set4 = {"apple", "banana", "cherry"}

myset = set1 | set2 | set3 | set4
print(myset)

my_newset = set1.union(set2)
print(my_newset)

my_newset.update(set3)
print(my_newset)

my_anotherset = set1.intersection(set2)
print(my_anotherset)

new_set = set2.intersection_update(set1)
print(new_set)