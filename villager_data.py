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
#create an list and inside of it create the same aumont of empty list according to the number of hobbys.
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


    vilagers_names_by_hobbys = [[], [], [], [], [], []]   #declared a list that takes in empty lists to hold the names by hobby.
    hobby_file = open(filename) #opening the file ans saving to a variable.

    for line in hobby_file: # iterating through the file.
        elements = line.split("|") #splitting each element in the line at the given separater.
        name = elements[0] #saving the element name to avariable.
        hobby = elements[3] #saving the element hobby to a variable.
        # print(hobby) #testing the code I have so far.
        if hobby == "Fitness": # this block of code is checking the hobbys and append the villagers name to them specific hobby list.
            vilagers_names_by_hobbys[0].append(name) #appending the owner hobby's name to them specific list.
    # print(vilagers_names_by_hobbys) #testing
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

    for group_hobby in vilagers_names_by_hobbys: #checking each child list from parent list.
        group_hobby.sort()               #sorting the child list in alphabetic order in place.

    return vilagers_names_by_hobbys #returning parent list with all the villagers names on it.

group_hobbys = all_names_by_hobby("villagers.csv") #assignin the function call to a variable 
# print(group_hobbys) #calling the function

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

    # TODO: replace this with your code

#pseudocode :
#create an empty list
#open the file
#iterate through the file
#split the string at the given separater and save it to a variable
#save each line as a tuple
#append each tuple to the empty list
#return the  list with the tuple in it.   

    all_data_in_the_file = [] #defining an empty listo to hold all the tupes
    with open(filename) as villagers_data: #openning the file and saving it to a variable

        for line in villagers_data.readlines(): #reading each file's line       
            line = line.replace("\n", "") #the original had this line breaker that we don't need / want to our list, so I just replaced it.
            elements = line.split("|") #spliting each line of string on the given delimiter
            each_line_as_tuple = tuple(elements) #saving each line as tuple
            # print(each_line_as_tuple) #testing the code so far
            all_data_in_the_file.append(each_line_as_tuple) #appending each line as tuple to the list
        # print(all_data_in_the_file)  #testing

    return all_data_in_the_file # returning the list of tuples

all_data_function = all_data("villagers.csv") #storing the function call to a variable
# print(all_data_function) #calling the function








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

    #pseudocode:
    #open the file
    #iterate through each line end read it
    #split the string at the given separater and save it to a variable
    #check if the element name is qual to given name
    #if true, returns its name
    #return none otherwise
    #call the function

    with open(filename) as file_villagers_informations:      #Opening the file and saving to a variable

        for line in file_villagers_informations.readlines(): #iterating over each line and reading it        
            elements = line.split("|") #spliting each line string in the given separator

            if elements[0] == villager_name: # checking if element name is equal to given name
                return villager_name #returning name if true
    
        return "None" returning none otherwise

look_for_motto = find_motto("villagers.csv", "motto") #saving the function call to an variable
print(look_for_motto)    #calling the function   










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
