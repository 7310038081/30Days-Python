# A Spam comment is defined as a text containing following keywords. "Make a lot of money","buy now","subscribe this","click this".Write a 
# program to detect these spams 

s1 = "Make a lot of money"
s2 = "buy now"
s3 = "subscribe this"
s4 = "click this"

message = input("Enter the message:")

if((s1 in message) or (s2 in message) or (s3 in message) or (s4 in message)):
    print("This is a spam message:")
else:
    print("This is not a spam message:")