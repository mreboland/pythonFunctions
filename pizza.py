# Passing an arbitrary number of arguments
# Sometimes you won't know ahead of time how many arguments a function needs to accept. Python allows a function to collect an arbitrary number of arguments from the calling statement

# The asterisk in the parameter name tells Python to make an empty tuple called toppings and pack whatever values it receives into this tuple (a list that can't be modified, uses brackets)
def makePizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)
    
makePizza("pepperoni")
makePizza('mushrooms', 'green peppers', 'extra cheese')
# outputs: (the both of which are tuples as it uses () brackets)
# ('pepperoni',)
# ('mushrooms', 'green peppers', 'extra cheese')

# To expand:

def makePizza(*toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a pizza with the following toppings:")
    # Create a loop to print each topping individually
    for topping in toppings:
        print(topping)


makePizza("pepperoni")
makePizza('mushrooms', 'green peppers', 'extra cheese')

# Mixing positional and arbitrary arguments
# If we want a function to accept several different kinds of arguments, the parameter that accpets an arbitrary number of arguments must be placed last in the function definition

def makePizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(topping)

# In the function definition, python assigns the first value it receives to the param 'size'. All other values that come after are store in the tuple 'toppings'.
makePizza(16, "pepperoni")
makePizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# You’ll often see the generic parameter name *args, which collects arbitrary positional arguments like this.

# Using arbitrary keyword arguments
# Sometimes you'll want to accept and arbitrary number of arguments, but you won't know ahead of time what kind of info will be passed to the function. In this case, you can write functions that accept as many key-value pairs as the calling statement provides

# The double asterisks in the paremeter tells python to create an empty dictionary with the variable given after the **
def buildProfile(first, last, **userInfo):
    """Build a dictionary containing everything we know about a user."""
    # Adding the first and last name given into the dictionary userInfo which is created by the **
    userInfo["firstName"] = first
    userInfo["lastName"] = last
    # return the data to the variable we set the call to
    return userInfo

# Calling the function and saving the return value to userProfile
userProfile = buildProfile(
    # first name
    "albert",
    # last name
    "einstein",
    # the next two are passed into the dict userInfo as key-value pairs
    location="princeton",
    field="physics"
)

print(userProfile)

# You’ll often see the parameter name **kwargs used to collect non-specific keyword arguments.

# 8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time.

def toppings(*ingreds):
    print("\nYou want a sandwhich with these toppings:")
    for ingred in ingreds:
        print(ingred)
        
toppings("lettuce", "tomato")
toppings("bread", "pickles", "cheese")
toppings("spam")

# 8-13. User Profile: Start with a copy of user_profile.py from page 149. Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.

def buildProfile(first, last, **userInfo):
    userInfo["firstName"] = first
    userInfo["lastName"] = last
    return userInfo

myProfile = buildProfile(
    "john",
    "doe",
    location="mystery",
    age=666,
    sex="male"
)

print(myProfile)

# 8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature. Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was
# stored correctly.

def makeCars(manufacturer, model, **carInfo):
    # adding the required info to the dict carInfo
    carInfo["brand"] = manufacturer
    carInfo["model"] = model
    # Returning the dict on call
    return carInfo
    
car = makeCars(
    "subaru",
    "outback",
    colour="blue",
    towPackage=True
)
print(car)
