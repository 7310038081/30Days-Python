# Write a program to print the following star pattern. 
#   * 
#  *** 
# ***** for n = 3  

# n = 3
# for i in range(1,n+15):
#     print("*")
    
n = int(input("Enter the number:"))
for i in range(1,n+1):
    print(" "*(n-i),end='')
    print("*"*(2*i-1),end="")
    print("")




# list1 = ["Data-Science", "Power BI", "Python"]

# for index, subject in enumerate(list1):
#     print(f"Index: {index}, Subj: {subject}")