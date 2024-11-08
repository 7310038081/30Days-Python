# Write a program to print multiplication table of a given number using while loop. 

n = int(input("Enter the number for which you want multiplication table:"))

i = 1
while (i<=n) :
    print(f"{n}X{i}={n*i}")
    i = i+1