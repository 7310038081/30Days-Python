#write a program to find out whether a student has passed or failed if it requires a total of 40% and atleast 33%in each subject to pass.
# Assume 3 subjects and take marks as an input from the user.


marks1 = int(input("Enter the marks:"))
marks2 = int(input("Enter the marks:"))
marks3 = int(input("Enter the marks:"))

Total_percentage = (100*(marks1+marks2+marks3)/300)

if(Total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are pass",Total_percentage)

else:
    print("You Failed!",Total_percentage)
