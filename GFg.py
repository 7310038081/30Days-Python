# You are given a number n, you need to print its multiplication table in a single line.

# Note: Please go through the range function in the video tutorial(for Python).

def utility():
    n=int(input())
    ## in is a membership operator that is true if something is a member of sequence
    for i in range(1,11): ## i in range(x,y,z) means i goes from x to y-1 and increments z steps in each iteration
        print(i*n, end=" ") ## Separating by spaces using end =" "
        
# You are given a String S, you need to print its characters at even indices(index starts at 0).

def utility(s):
    # Iterate over the list `s`
    for i in range(len(s)):  # Use the index to access the list elements
        if i % 2 == 0:  # Check if the element is even
            print(s[i],end='')  # Print the even element

# Given a number x, the task is to print the numbers from x to 0 in decreasing order in a single line.
# Function to print x in decreasing order
def utility(x):
    # Complete the code 
    i = 0 
    while(i>=0 and x>=0):
        print(x,end=' ')
        x = x-1