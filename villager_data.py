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
        # print(species)
        # if species == search_string:
        #     # print(name)
        #     villagers.append(name)
        # elif 
        #     villagers.append(name)       
    return sorted(villagers)

print(get_villagers_by_species("villagers.csv", "Tiger"))   





def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # TODO: replace this with your code

    hobbys = ["Fitness", "Nature", "Education", "Music", "Fashion", "Play"]
    group_hobby = []

    hobby_file = open(filename)
    for line in hobby_file:
        elements = line.split("|")
        name = elements[0]
        hobby = elements[3]
        # print(hobby)
        if hobby == "Fitness":
            group_hobby.append(name)
    # print(group_hobby) 
        if hobby == "Nature":
            group_hobby.append(name)
    return [group_hobby]
# print(all_names_by_hobby("villagers.csv"))    


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
