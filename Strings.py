#Strings are sequence of characters enclosed with quotes . They are immutable ,meaning they cannot be changed once they are initialized
# common methods:

# 1.len(s): Returns the length of the string.
s= "Hello World"
print(len(s))

# 2.lower() Converts all characters to lowercase.
a = "HELLO AMAN"
print(a.lower())

# 3.upper() Converts all characters to uppercase.
b = "hello vivek"
print(b.upper())

# 4.replace(old,new) Replaces occurrences of a substring.
c = "aman singh"
value = c.replace("aman","vivek k ")
print(value)

f = "aman   singh   vivek   singh"
value2 = f.replace("   ","")
print("the value of f is ",value2)


# 5.split() Splits the string into a list based on a separator.
d = "aman_singh_vivek_singh"
value1 = d.split("_")  #split the string into a list based on a separator 
print(value1)

# 6.strip() Removes leading and trailing whitespace.
e = "      -amansinghviveksingh-    "
print(e)
#after applying the strip 
print(e.strip())

# 7.find() Returns the index of the first occurrence of a substring; returns -1 if not found
g = "aman singh vivek singh"
value3 = g.find("vivek")
value4 = g.find("pritika")
print(value3,value4)

# 8.join() Joins elements of an iterable into a single string, using the string as a separator.
h = ['aman','singh','vivek','singh']
value5 = ' '.join(h)
print(value5)