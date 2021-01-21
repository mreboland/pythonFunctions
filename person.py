# Returning a dictionary
# A function can return any kind of value you need it to, including more complicated data structure like lists and dictionaries.
def buildPerson(firstname, lastname):
    """Return a dictionary of information about a person"""
    # The function take a persons name and puts the values into the dictionary below. Using first and last as the key, the firstname, lastname as their values respectively
    person = {"first": firstname, "last": lastname}
    return person

musician = buildPerson("jimi", "hendrix")
print(musician)

# Expanding on the above to include optional info
# The value None is used when a variable has no specific value assigned to it. Think of it as a placeholder value. In conditional tests, None evaluated to False.
def buildPerson(firstname, lastname, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': firstname, 'last': lastname}
    # age=None is False so if no age is given the below code is ignored and we return person.
    if age:
        # If age does exist, add it to the dictionary
        person['age'] = age
    return person

musician = buildPerson('jimi', 'hendrix', age=27)
print(musician)
musician = buildPerson('jimi', 'hendrix')
print(musician)
