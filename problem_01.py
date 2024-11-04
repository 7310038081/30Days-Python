#write a program to find the greatest of four numbers entered by the user . 

a = int(input("Enter the number1:"))
b = int(input("Enter the number2:"))
c = int(input("Enter the number3:"))
d = int(input("Enter the number4:"))

if(a>b and a>c and a>d):
    print(a)
elif(b>a and b>c and b>d):
    print(b)
elif(c>a and c>b and c>d):
    print(c)
else:
    print(d)


