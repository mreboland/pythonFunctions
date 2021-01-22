# 8-15. Printing Models: Put the functions for the example printing_models.py in 
# a separate file called printing_functions.py. Write an import statement at the 
# top of printing_models.py, and modify the file to use the imported functions.


# Pulled from printingModels.py
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
