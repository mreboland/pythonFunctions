# Return values
# A function doesn't always have to display its output directly. Instead it canprocess some data and then return a value or set of values. The value the function returns is called a return value. The return statement takes a value from inside a function and sends it back to the line that called the function. Return values allow us to move much of the program's grunt work into functions, which can simplify the body of your program.

# Returning a simple value

# create a function with two parameters to pass data
def getFormattedName(firstname, lastname):
    """Return a full name, neatly formatted."""
    # Create a variable to save the data to
    fullname = f"{firstname} {lastname}"
    # we convert the variable fullname to title case and return it to the calling line
    return fullname.title()

# The return in the function is sent back to the call below and is save to the variable musician
musician = getFormattedName("jimi", "hendrix")
# Print the name of the musician
print(musician)

# Writting all the above is a lot of code just for one name. It comes in handy when you're dealing with lots of data and you call the function for a list of names for example.

# Making an argument optional
# Sometimes it makes sense to make an argument optional so that people using the function can choose to provide extra info only if they want to. We can use default values to make an argument optional.
def getFormattedName(firstname, middlename, lastname):
    """Return a full name, neatly formatted."""
    fullname = f"{firstname} {middlename} {lastname}"
    return fullname.title()

# The function works like usual when given all three names of a person. But a lot of the time a middle name isn't necessary so how do we solve it?
musician = getFormattedName("john", "lee", "hooker")
print(musician)

# To solve the issue of not needing a middle name all the time we set the parameter to equal an empty string or default value. We move it to the end of the paramenter line for reasons mentioned earlier (order of arguments)
def getFormattedName(firstname, lastname, middlename=""):
    """Return a full name, neatly formatted."""
    # We create an if statement here to check for a middle name because if we don't, on the output there will be an extra space that the middlename would occupied so there'd be 3 spaces between first and last instead of 2
    # If middlename is true proceed to include it
    if middlename:
        fullname = f"{firstname} {middlename} {lastname}"
    # If middle name is false (empty) proceed here
    else:
        fullname = f"{firstname} {lastname}"
        
    return fullname.title()

musician = getFormattedName('jimi', 'hendrix')
print(musician)
musician = getFormattedName('john', 'hooker', 'lee')
print(musician)
