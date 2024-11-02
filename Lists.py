# Lists are ordered, mutable collections that can hold items of different data types. 
# They are defined using square brackets

# 1.append() Adds an item to the end of the list.
l1 = []
l1.append("vivek")
print(l1)

l1.append("singh")
print(l1)

# 2.extend([,]) Extends the list by appending elements from an iterable

l1.extend(["aman","singh"])
print(l1)  

# 3.insert()  Inserts an item at a specified index.
l1.insert(2,"pritika")
print(l1)

# 4.remove()  Removes the first occurrence of an item.
l1.remove("pritika")
print(l1)

# 5.pop() Removes and returns the item at the specified index.
l1.pop(1)
print(l1)

# 6.sort() Sorts the list in ascending order.
l2 = [6,4,2,1,5,8,3,0]
l2.sort()
print(l2)

# 7.reverse() reverse the list 
l3 = [1,2,3,4,5,6]
l3.reverse()
print(l3)

# 8.index() Returns the index of the first occurrence of an item
value =l3.index(3)
print(value)

# 9.Count() Returns the number of occurrences of an item
l4 = [1,1,2,3,4,5]
print(l4.count(1))