n = 12

for i in range(1,11):
 result = print(str(n)+ 'x' + str(i)+'='+str(n*i))

print(result)

#print the numbers in the table of 23 which are divisble by 5

n = 23
for i in range(1 ,11):
 number = n *i
if(number%5==0):
    print(number)

#print the number  between 0-100 that are divisble by 5 & 2

count = 0
for i in range(0,101):
 if(i%5==0 )and (i%2==0):
  print(i)
  count = count + 1

print(count)

n = int(input("Enter the number: "))

for i in range(1,11):
    print(n*i)

for i in range(1,11,2):
    print(n,"*",i,"=",n*i)

# printing the table of 1 and 2 with the seperation of 2 

for i in range(1,21,2):
    print(i)

print('-'*20)

for i in range(2,21,2):
    print(i)


# printing the table with the for loop 

n = int(input("Enter the number: "))

for i in range(n,(n*10)+1,n):
    print(i)

# Nested for loop

for i in range(1,7):
  for j in range(1,7):
    for k in range(1,7):
     print(i,j,k)
  print("--------")
print("The loops is terminated")


# two dices was rolled what are the numbers that have sum of 5
for i in range(1,7):
    for j in range(1,7):
     if((i+j==5)):
        print(i,j)


number=0
for i  in range(1,7):
   for j in range(1,7):
      if((i+j)==8):
         print(i,j)
         number = number + 1


print(round(number/36*100,2))
  

for n in range(1,19):
    number = 0
    for i in range(1,7):
        for j in range(1,7):
            for k in range(1,7):
                if(i+j+k==n):
                    number = number + 1
    print(n,"=",round((number/216)*100,2))               
                  
