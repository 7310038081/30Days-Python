# name = input("Enter the name: ")

# #String Slicing
# string_slicing = name[0:3]
# print(string_slicing)
# print('_'*20)

# #String slicing with the skip value
# a = "0123456789"
# b = print(a[1:7:3])


# c = "abcdefghijklmnopqrstuvwxyz"
# d = print(c[0:9:4])
# print('_'*20)

# # String access
# nameshort1 = name[0] #to access the string through the index
# nameshort2 = name[1] #to access the string through the index
# nameshort3 = name[-1] #to access the string through the index
# nameshort4 = name[-2] #to access the string through the index
# print(nameshort1 ,nameshort2 , nameshort3 , nameshort4)
# print('_'*20)


# #To find the length of the string we use len function
# length = len(name)
# print(length)


##############################################################String Functions############################################################

#len("string")
# full_name = "Vivek Singh"
# Length = len(full_name)
# print(Length)


#.endswith(" ")
# name = "vivek"
# print(name.endswith("vk")) 
# print(name.endswith("vek"))


#.startswith(" ")
# name = "vivek"
# print(name.startswith("viv"))
# print(name.startswith("Viv")) # CASE SENSITIVE

#.capitalize("")
# name = "vivek"
# print(name.capitalize())

#.title("")
# name = "vivek singh aman singh"
# print(name.title())

#.lower()
# name = "VIVEK"
# print(name.lower())

#.upper()
# name = "vivek"
# print(name.upper())

#.strip()
# name = "    vivek  "
# print("my name is",name.strip())

#.split()
# name = "vivek singh"  # it converts the string into list based on the delimiter 
# print(name.split())   # by default delimiter is space

#.join()
# aman = ['vivek','singh']
# print("_" .join(aman))

#.replace()
# name = "vivek singh"
# print(name)
# print(name.replace("vivek", "Aman"))

#find()
# name = "vivek"
# print(name.find("k"))

#isdigit()
# digit3 = "123455"
# print(digit3.isdigit())
# digit1 = str(1234)
# print(digit1.isdigit())

#isalpha()
# name = "vivek"
# print(name.isalpha())
# digit = "123"
# print(digit.isalpha())

#isalnum()
# name = "#"
# print(name.isalnum())
# name1 = "vivek123"
# print(name1.isalnum())