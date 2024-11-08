# Write a program to find the sum of first n natural numbers using while loop. 
n = int(input("Enter the number:"))
sum = 0

i = 0

while(i<=n):
    sum = sum+i
    i = i+1;

print(sum)

# for i in range (1,n+1):
#     sum = sum + i
#     i = i+1
# print(sum)