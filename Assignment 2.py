# Write a Python program to print all positive numbers in a range.
#Input: list1=[12, -7, 5, 64, -14]. Output: 12, 5, 64
s=0
list1=[12, -7, 5, 64, -14] #Mentioned the list from which we have to select the positive values.
for i in list1:
    if i>0:                               # It will print only the values greater than 0. Not lesser than, so there can't be negative numbers.
        print(i)                        # The print statement will print only the positive numbers.

#Input: list2=[12, 14, -95, 3]. Output: [12, 14, 3]
s=0
list2=[12, 14, -95, 3]
for i in list2:
    if i>0:
        print(i)