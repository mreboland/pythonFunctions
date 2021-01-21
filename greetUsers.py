# Passing a list
# Passing a list to a function allow the function full access to the content of the list.
def greetUsers(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

# A list of names we want to pass to the function   
usernames = ["hannah", "ty", "margot"]
# We call the function and pass the argument which is the list of names. The list is pass directly as is, into the function. As such, in the function we need to loop over the list to access its info to print out the msg.
greetUsers(usernames)