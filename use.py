#reverse the number 

n = int(input("Enter the number:"))
y = 0

while(n!=0):
    x = n%10
    y = y*10 + x
    n = n//10

print(y)