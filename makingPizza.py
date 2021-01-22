# import tells python to read the file you specified
# https://stackoverflow.com/questions/52149113/import-a-file-from-another-directory
import makePizza

# The first name is the imported module, the second name if the function you want to call within that module
# module_name.function_name()
makePizza.makePizza(16, "pepperoni")
makePizza.makePizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Importing specific functions:
# from module_name import function_name

# Importing many functions:
# from module_name import function_0, function_1, function_2

# Using the above example of making pizza:
# from pizza import makePizza

# Using 'as' to give a function an alias
# If the name of a function we're importing might conflict with an existing name in our program (or if the name is too long), we can use an alias when we import the function
# from pizza import makePizza as mp
# mp(16, ...)
# mp(12, ...)

# The general syntax is:
# from module_name import function_name as fn

# Using 'as' to give a module an alias
# Same as giving a function an alias we can do the same with the module
# import pizza as p
# p.makePizza(16, ...)
# p.makePizza(12, ...)
# Doing the above is helpful as it makes the code more concise and it also shortens the module name moving our focus to the descriptive names of its functions (removes confusion)
# General syntax:
# import module_name as mn

# Importing all functions in a module
# We can tell python to import every function by using *
# from pizza import *
# The difference from 'import pizza' is that we don't need to use the dot notation with our functions, we can call it directly:
# makePizza(16, ...)
# makePizza(12, ...)
# The downside to this is if we are working with larger modules that we didn't write, there can be matching function names in the module to those in your project causing conflicts. This can result in python overwritting the functions with the same name. Its best to either import the function itself or use dot notation covered earlier.

# Styling functions

# Functions should use descriptive parameters that aren't vague.
# If providing a default value, no spaces should be included. The same applies for when you providing an argument with a value.
# def function_name(parameter_0, parameter_1='default value')
# function_name(value_0, parameter_1='value')
# If you're passing lots of arguments, you can indent to one level:
# def function_name(
#         parameter_0, parameter_1, parameter_2,
#         parameter_3, parameter_4, parameter_5):
#     function body...

# all import statements should be at the top of the file.