# String Concatenation
print('Vivek' + ' Singh')   #to concatenate the string we use the + opertor btw the string which we want to add
print('-'*30)

# String Replication
print("Vivek"*3)       #to replicate the string we multiply the string to n times 
print('-'*30)

# String Length
print(len("viveksingh"))  #to find the length of the string we use the length function
print('-'*30)

# String Slicing
print("VivekSingh" [2])  
print("VivekSingh" [-2])
print("VivekSingh" [-1])
print("Vivek Singh" [0:5]) #this is string slicing
print("Vivek Singh" [6:11])
print("Vivek Singh" [3:])
print('-'*30)

# String Case Conversion
print("VIVEKSINGH".lower())  #.lower()
print("viveksingh".upper())  #.upper()
print('-'*30)

# String Stripping 
print("     vivek singh     ")
print("         vivek singh         " .strip())  #strip function removes the unecessary spaces which are present in th string 
print('-'*30)

# String Replacing  
print("Vivek Singh" .replace('i','-'))
print("Vivek Singh" .replace('Viv','--'))
print('-'*30)


# String Count 
print("Vivek Singh")
print("Vivek Singh".count('V'))
print("Vivek Singh".lower().count('v'))
print("Vivek Singh".upper().count('V'))
print('-'*30)


#String Find
print("Vivek Singh".find("ek"))
print('-'*30)

# String Check
print("viveksingh".isalpha())
print('123'.isalpha())
print('123'.isdigit())
print("viveksingh".islower())
print("VIVEKSINGH".islower())
print("VIVEKSINGH".isupper())
print('-'*30)

#String Capitalization
print("vivek singh".capitalize())
print("vivek singh".title())
print('-'*30)

#String startwith or endwith 
print("Vivek Singh".startswith("Viv"))
print("Vivek Singh".endswith("snsj"))
print('-'*30)

#String adjust center , left , right 
print("Vivek Singh".center(20,"*"))
print("Vivek Singh".ljust(20,"*"))
print("Vivek Singh".rjust(20,"*"))