# WAPS to accept a filename from the user and print the extension of that.
file= input("Input the filename: ")
file=file.split(".")
print ("Extension of the file is: "+ file[-1])