thsislist = ["apple", "banana", "orange", "grapes", "pomegranade", "cherry"]
thsislist.append("new_item")
new_arr = ["item1", "item2", "item3"]
new_tuple = ("item1", "item2", "item3")
thsislist.extend(new_arr)
thsislist.extend(new_tuple)
print(thsislist)