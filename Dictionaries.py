  # Dictionaries are unordered collections of key-value pairs. They are mutable and defined using curly braces.
my_dict = {'name':"aman",'age':23}

# 1.keys() Returns a view of the dictionary’s keys.
print(my_dict.keys())

# 2.value() Returns a view of the dictionary’s values.
print(my_dict.values())

# 3.items() Returns a view of the dictionary’s key-value pairs.
print(my_dict.items())

# 4.get(key) Returns the value for the specified key.
print(my_dict.get('name'))

# 5.pop(key) Removes the specified key and returns its value.
age = my_dict.pop('age')
print(age)
print(my_dict)

# 6.update() Updates the dictionary with key-value pairs from another dictionary or iterable.
my_dict.update({'age':24})
print(my_dict)

# 7.clear() Removes all items from the dictionary.
my_dict.clear()
print(my_dict)
