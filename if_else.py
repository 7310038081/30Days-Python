# n = int(input('Enter the number: '))    #if else statements

# if(n>0):
#     print(n,'the number is +ve')
# elif(n==0):
#     print(n,'the number is zero')
# else:
#     print(n,'the number is -ve')

n = float(input("Enter the number: "))

# if(n%5==0):
#     if(n%3==0):
#        print("The number is divisible by 5 and 3")
#     else:
#         print("The number is not divisble by 3 and 5")

# else:
#     print("The number is not divisble by 5")

if(n%5==0) and (n%3==0):
    print("The number is divisible by 5 and 3")

else:
    print("The number is not divisible by 5 and 3")