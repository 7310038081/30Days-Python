# # list is a collection of differnt type of data 

# # reverse a list
# lst = ['vivek','shobhit','aman','aradhya','pritika']
# print(lst)
# print()

# print(lst[::-1])
# print()

# print(lst[::-2])
# print()

# print(lst[0::])

# # #append
# lst.append("Vivek")
# print(lst)
# print()

# # #remove
# lst.remove("Vivek")
# print(lst)
# print()

# # #sorted
# lst1 = [4,3,5,2,7,9,0,1]
# lst1.sort()
# print(lst1)
# print()

# #index
# value =lst1.index(5)
# print(value)
# print()

# #count
# lst2 = [1,1,2,2,1,1,2,3]
# print(lst2.count(1))
# print()

# #extend can add multiple values at a time 
# lst3 = [2,2,3,3]
# lst3.extend([4,4,5,5,'vivek','aman'])
# print(lst3)
# print()

# #max
# lst4 = [1,8,33,87,65,99]
# print(max(lst4))
# print()

# #min
# print(min(lst4))

# lst5 = [9,8,7,6,5,4,3,2,1,0]

# for i in range(len(lst5)-1,-1,-1): #reverse 
#     print(lst5[i],end=' ')
    
# print("\n")


# for i  in range(len(lst5)):
#     print(lst5[i],end =' ')
# print("\n")

# for i in lst5:
#     print(i, end = ' ')


#multidimensional list

lst = [["vivek","shobhit",1,2],["pritika","aman",3,4]]
# print(lst[0][1])


# accessing all the elements in the multidimensional list
for i in lst:
    for j in i:
        print(j)
