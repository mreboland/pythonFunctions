# Modifying a list in a function
# When you pass a list to a function, the function can modify the list. Any changes made to the list inside the function’s body are permanent, allowing you to work efficiently even when you’re dealing with large amounts of data.
# Start with some designs that need to be printed
unprintedDesigns = ['phone case', 'robot pendant', 'dodecahedron']
completedModels = []

# Simulate printing each design, until non are left
# Move each design to completedModels after printing
while unprintedDesigns:
    # remove value from list using pop (last item)
    currentDesign = unprintedDesigns.pop()
    # print that we are working on design
    print(f"Printing model: {currentDesign}")
    # once done, we add, append the value from currentDesign to completedModels
    completedModels.append(currentDesign)
    
# Display all completed models
print("\nThe following models have been printed:")
for completedModel in completedModels:
    print(completedModel)

# We've seen the above code in a similar example before, however it's not using a function. Modifying it so it does using two functions:

# Defining the function that will take in both our lists we want to modify
def printModels(unprintedDesigns, completedModels):
    # Simulate printing each design, until non are left
    # Move each design to completedModels after printing
    while unprintedDesigns:
        # remove value from list using pop (last item)
        currentDesign = unprintedDesigns.pop()
        # print that we are working on design
        print(f"Printing model: {currentDesign}")
        # once done, we add, append the value from currentDesign to completedModels
        completedModels.append(currentDesign)

# Our second function will be called once the first is done with the data so we can print it out using the list completedModels
def showCompletedModels(completedModels):
    # Display all completed models
    print("\nThe following models have been printed:")
    for completedModel in completedModels:
        print(completedModel)

unprintedDesigns = ['phone case', 'robot pendant', 'dodecahedron']
completedModels = []

# Pass our lists to printModels
printModels(unprintedDesigns, completedModels)
# Call the below to print out our new, modified list
showCompletedModels(completedModels)

# It's good practice to have a function do 1 job. If you are writting a function and it's doing too many different tasks, try to split up the code. Remember you can always call a function from another function, which can be helpful when splitting a complex task into a series of steps.

# Preventing a function from modifying a list
# In our previous example, unprintedDesigns becomes empty after the printModels function is run with it. What if you want to keep the data in it?
# If we go back to earlier lessons, we know that using a slice [:] takes a copy of a list
# Using our previous example:
# printModels(unprintedDesigns[:], completedModels)
# The above will take a copy of unprintedDesigns and leave the original

# It's good practice however to use the original, and only use a copy when absolutely necessary. The latter of which takes more time and memory to make the copy and can be an issue with large lists.

# 8-9. Messages: Make a list containing a series of short text messages. Pass the
# list to a function called show_messages(), which prints each text message.

textMessages = ["hello", "goodbye", "go away"]

def showMessages(messages):
    for message in messages:
        print(message)
        
showMessages(textMessages)

# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed. After
# calling the function, print both of your lists to make sure the messages were
# moved correctly.

textMessages = ["hello", "goodbye", "go away"]
sentMessages = []

def sendMessages(textMessages, sentMessages):
    while textMessages:
        message = textMessages.pop()
        print(f"\nSending: {message}")
        sentMessages.append(message)

def showMessages(messages):
        print(messages)
    # for message in messages:

sendMessages(textMessages, sentMessages)
showMessages(textMessages)
showMessages(sentMessages)

# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the
# function send_messages() with a copy of the list of messages. After calling the
# function, print both of your lists to show that the original list has retained its
# messages.
textMessages = ["hello", "goodbye", "go away"]
sentMessages = []

sendMessages(textMessages[:], sentMessages)
print(textMessages)
print(sentMessages)
