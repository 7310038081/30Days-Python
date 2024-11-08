# Write a program to find whether a given number is prime or not. 
import math

n = int(input("Enter the number: "))

# Step 1: Handle edge cases for numbers less than or equal to 1
if n <= 1:
    print("Less than or equal to 1 is not prime")
elif n == 2:
    print("2 is a prime number")  # 2 is the only even prime number
else:

    for i in range(2,n):
        if n % i == 0:  # If n is divisible by i, it is not prime
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")  # If no divisors were found, it's prime
