'''Write Python code to create a function called most_frequent that takes a string
and prints the letters in decreasing order of frequency. Use dictionaries.

Your Input and output should look something like this:
Input: Please enter a string Mississippi
Output: i = 04 s = 04 p =02 m =01'''

def most_frequent(): # Storing the value of Mississippi in a function called "most_frequent".
    print("Mississippi")
txt = "Mississippi" # Using the count method to count each of the letters in the word Mississippi.
g=txt.count("i")
h=txt.count("s")
i=txt.count("p")
j=txt.count("M")
a=str(input("Enter the string Mississippi: "))
if a=="Mississippi": # If the entered word is Mississippi, the code will print the word and number of time a letter occurs.
    most_frequent()
    print('i =',g,', s =',h,', p =',i,', m =',j) # Shows the number of times a letter occurs.
else:
    print("Error") # If the entered word is not Mississippi, the code will print error.