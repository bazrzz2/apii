filename = "file.txt" # replace with the name of your file
search_var = "my_variable" # replace with the variable you want to search for

# open the file in read mode
with open(filename, 'r') as file:
    # read the contents of the file
    contents = file.read()
    # check if the variable is in the file
    if search_var in contents:
        print("yes")
    else:
        print("no")