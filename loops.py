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

