"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    species = set()

    # TODO: replace this with your code

    villager_records = open(filename)
    for line in villager_records:
        separate_line = line.split("|")        
        unique_species_index = separate_line[1]
        species.add(unique_species_index) 
        
    return species

# print(all_species("villagers.csv"))


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names    """

    villagers = []

    # TODO: replace this with your code

    villagers_name = open(filename)
    for line in villagers_name:
        element = line.split("|")
        name = element[0]
        species = element[1]
        if search_string == "All":
            villagers.append(name)
        elif species == search_string:
            villagers.append(name)   
    return sorted(villagers)

# print(get_villagers_by_species("villagers.csv", "Tiger"))   





def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # TODO: replace this with your code

#pseudocode:
#create an list and inside of it create the same aumont of empty list according to the number of hobbys?
#open the file
#iterate over the list
#separate each element of the string in the given delimiter
#save the villager's name index to a variable
#save the villager's hobby index to a variable
#check which vilagers has the specific hobby and append it to the specific list
#return the empyt list you first created "but now is not empty anymore"


#sorting by alphabetic order:
#iteraght through the each element at the list
#sort each list in alphabetic order

#testing the function
#assign the function call to a variable (Store information about names group by hobby into a list)
#iterate through the function call (Iterate through list from above)
#print every element in separate line (Print every list element separated by newline) 



    vilagers_names_by_hobbys = [[], [], [], [], [], []]   
    hobby_file = open(filename)

    for line in hobby_file:
        elements = line.split("|")
        name = elements[0]
        hobby = elements[3]
        # print(hobby)
        if hobby == "Fitness":
            vilagers_names_by_hobbys[0].append(name)
    # print(vilagers_names_by_hobbys) 
        if hobby == "Nature":
            vilagers_names_by_hobbys[1].append(name)
        if hobby == "Education":
            vilagers_names_by_hobbys[2].append(name)    
        if hobby == "Music":
            vilagers_names_by_hobbys[3].append(name)   
        if hobby == "Fashion":
            vilagers_names_by_hobbys[4].append(name)   
        if hobby == "Play":
            vilagers_names_by_hobbys[5].append(name)  

    for group_hobby in vilagers_names_by_hobbys:
        group_hobby.sort()               

    return vilagers_names_by_hobbys

group_hobbys = all_names_by_hobby("villagers.csv")
print(group_hobbys)

# for group_hobby in group_hobbys:  #testing the code printing every list element separated by newline.
#     #group_hobby.sort()
#     print(group_hobby)
#     print()



 


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
