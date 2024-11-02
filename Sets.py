# Sets are unordered collections of unique items, defined using curly braces or the set() function. They are mutable.
set1 = {1,2,3,7,9,10}
# 1.add(item): Adds an item to the set.
set1 = {1,2,3,7}
set1.add(4)
print(set1)

# 2.remove(item): Removes an item from the set; raises KeyError if not found.
set1.remove(4)
print(set1)

# 3.discard(item): Removes an item without raising an error if not found.
set1.discard(5)
print(set1)

# 4.union(other_set): Returns the union of two sets.
set2 = {2,4,5,6,8}
value = set1.union(set2)
print(value)

# 5.intersection(other_set): Returns the intersection of two sets.
print(set1.intersection(set2))

# 6.difference(other_set): Returns the difference between two sets.
print(set1.difference(set2))

# 7.clear(): Removes all items from the set.
set1.clear()
print(set1)

# Strings: Immutable sequences of characters, with methods for manipulation.
# Lists: Mutable ordered collections, allowing dynamic modifications.
# Tuples: Immutable ordered collections, suitable for fixed data.
# Dictionaries: Mutable collections of key-value pairs, offering fast access.
# Sets: Mutable collections of unique items, useful for set operations.