#  Write a program to find out whether a given post is talking about “Vivek” or not. 

post = input("Enter the sentence here:")

if("Vivek".lower() in post.lower()):
    print("Vivek name is in post")
else:
    print("Vivek name is not in post")