#write a program which finds out whether a given username is present in a list or not 
username = input("Enter the username:")

list1 = ["vivek singh","aman singh","pritika singh","shobhit singh"]

if(username in list1):
    print("Username present in the list")
else:
    print("Username not present in the list")