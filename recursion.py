# when a function call itself is called recursion

# write a function for factorial using recursion 

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

n = int(input("Enter the number:"))
print(f"The factorial is,{factorial(n)}")

