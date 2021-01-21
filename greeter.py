# Defining a funtion

# def lets python know you are defining a function. The word following the def is the function's name, which is a variable you create. The brackets will hold information that the function needs. When we call the function at the end of the program we'd put info in the brackets if we needed it passed to the function. You'd put a variable in the functions brackets in order to pass the info along in the functions code. It our case we don't need any additional info so we leave it blank for both the call and the function itself.
def greetUser():
    # The triple quotes is a docstring which python looks for when it generates documentation for the functions in your program
    """ Display a simple greeting """
    print("Hello!")

# Calling the function without passing any info
greetUser()

# Passing info to a function

# Function has a username (or parameter) in the brackets which means the function needs to be passed info in order to work. If it's left out in the call, the function will kick out a type error.
def greetUser(username):
    """Display a simple greeting"""
    # We use 'username' in order to pass the info from the call into the function
    print(f"\nHello, {username.title()}!")

# Call the function and passing it a name (called and argument).
greetUser("billy")

# We call the function with an argument. The argument is passed into the parementer we defined (as a variable) of the function which is then used to manipulate code in the function.

# People sometimes speak of arguments and parameters interchangeably. Don’t be surprised if you see the variables in a function definition referred to as arguments or the variables in a function call referred to as parameters.


# 8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the
# function, and make sure the message displays correctly.

def displayMessage():
    print("\nWe are learning about functions in this chapter!")
    
displayMessage()

# 8-2. Favorite Book: Write a function called favorite_book() that accepts one
# parameter, title. The function should print a message, such as One of my
# favorite books is Alice in Wonderland. Call the function, making sure to
# include a book title as an argument in the function call.

def favouriteBook(title):
    print(f"\nOne of my favourite books is {title.title()}!")
    
favouriteBook("Wheel of Time")

# Passing arguments
# Because a function definition can have multiple parameters, a function call may need multiple arguments. You can pass arguments to your functions in a number of ways. You can use positional arguments, which need to be in the same order the parameters were written keyword arguments, where each argument consists of a variable name and a value and lists and dictionaries of values. Let’s look at each of these in turn.
    
# Positional arguments
# Passing arguments in the order they are written

# Here we have two parameters that we will use to generate a message from
def describePet(animalType, petName):
    """Display info about a pet."""
    print(f"\nI have a {animalType}.")
    print(f"\nMy {animalType}'s name is {petName.title()}.")

# Because we wrote our function with two parameters, we need to call the function with two arguments. The arguments need to be passed in the order of the function parameters
describePet("hamster", "harry")

# Multiple function calls
# We can call the function as many times as we want
describePet("dog", "sir barks a lot")

# Order matters in positional arguments

# If we were to call our function above with reversed info
describePet("harry", "hamster")
# Our function would output our sentence in reverse order giving us a backwards sentence.
# I have a harry.
# My harry's name is Hamster.
# Be mindful of your argument order

# Keyword arguments
# A keyword argument is a name-value pair that you pass to a function. You directly associate the name and the value within the argument, so when you pass the argument to the function, there's no confusion.
def describePet(animalType, petName):

    """Display information about a pet."""
    print(f"\nI have a {animalType}.")
    print(f"My {animalType}'s name is {petName.title()}.")

# By using the parameter names as arguments and making them equal to the value we want, it removes any confusion about where the data is going and what it's for.
describePet(animalType="hamster", petName="harry")
# Because we use the parameter names, the order doesn't matter either when we call the function. It'll still output correctly
describePet(petName="harry", animalType="hamster")
# When using keyword arguments, be mindful of spelling and that the arguments match the parameters

# Default values
# When writing a function, you can define a default value for each parameter. If an argument for a parameter is provided in the function call python will use that. If it's not, python will use the default value we set for the parameter. Which means it can be left out in the call if the parameter doesn't need new data.
# Note that the order of the parameters in the function definition had to be changed from earlier. Because the default value makes it unnecessary to specify a type of animal as an argument, the only argument left in the function call is the pet’s name. Python still interprets this as a positional argument, so if the function is called with just a pet’s name, that argument will match up with the first parameter listed in the function’s definition. This is the reason the first parameter needs to be petName.
def describePet(petName, animalType="dog"):
    """Display information about a pet."""
    print(f"\nI have a {animalType}.")
    print(f"My {animalType}'s name is {petName.title()}.")

# We left out the argument for animalType so it's value defaulted to dog and the function used 'willie' for the name
describePet(petName="willie")
# We can override the default value by adding the argument for animalType:
describePet(petName="willie", animalType="orca")

# When you use default values, any parameter with a default value needs to be listed after all the parameters that don’t have default values. This allows Python to continue interpreting positional arguments correctly.

# Equivalent function calls
# Because positional arguments, keyword arguments, and default values can all be used together, often you’ll have several equivalent ways to call a function.
# def describePet(pet_name, animal_type='dog'):

# A dog named Willie.
# describePet('willie')
# describePet(pet_name='willie')

# A hamster named Harry.
# describePet('harry', 'hamster')
# describePet(pet_name='harry', animal_type='hamster')
# describePet(animal_type='hamster', pet_name='harry')

# It doesn’t really matter which calling style you use. As long as your function calls produce the output you want, just use the style you find easiest to understand.

# Avoiding Argument Errors
# When you start to use functions, don’t be surprised if you encounter errors
# about unmatched arguments. Unmatched arguments occur when you provide fewer or more arguments than a function needs to do its work.


def describePet(animalType, petName):
    """Display info about a pet."""
    print(f"\nI have a {animalType}.")
    print(f"\nMy {animalType}'s name is {petName.title()}.")
    
# By calling the function that has parameters without arguments will result in a type error about required positional arguments. This also applies if you give to many arguments for the amount of parameters in the function
# Python helps us out by listing the arguments that weren't passed to the function. This is a good reason to have good naming schemes for our arguments so we know what it's for.
# describePet()


# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

def makeShirt(size, text):
    print(f"\nYou've select a size {size}, with '{text}' written on it")
    
makeShirt("large", "Python is the best!")
makeShirt(size="large", text="Python is the best!")

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.


def makeShirt(text, size="large"):
    print(f"\nYou've select a size {size}, with '{text}' written on it")
    
makeShirt("I love Python")
makeShirt("I love Python", "medium")
makeShirt("Python rules!", "small")

# 8-5. Cities: Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the default country.
def describeCity(name, country="canada"):
    print(f"\n{name.title()} is in {country.title()}.")
    
describeCity("toronto")
describeCity("ottawa")
describeCity("tokyo", "japan")
describeCity("saigon", "vietnam")
