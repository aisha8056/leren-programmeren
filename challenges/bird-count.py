bird_list = [{'name': 'mus', 'key': 'm', 'count': 0},
             {'name': 'duif', 'key': 'd', 'count': 0},
             {'name': 'koolmees', 'key': 'k', 'count': 0},
             {'name': 'kraai', 'key': 'i', 'count': 0},
             ]

print('Bird counter until dot')

#REVISION: The def keyword is used to create, (or define) a function.



# TO DO:

# 1) print all birds with key and name which is using bird_list and key together. 

# In this code it will Loop through each bird in the bird_list, print its key and name
for bird in bird_list:
    print(f"{bird['key']}: {bird['name']}")

#in this code the def is bascially making a new fuction and 
# 2) define function get_bird_by_key(birds: list, key:str) returns bird or None

def get_bird_by_key(bird_list, key):  # Loop through each bird type in the list
    for bird in bird_list:
        if bird['key'] == key:  # If the bird's "key" value matches the given "key", return the entire bird type
            return bird
    return None  # If no matching bird is found, return None


# 3) repeat until given '.'
#       input key of bird 
#    find bird with get_bird_by_key
#    if bird found: 
#       increment bird count
#       show bird name and count




# 4) print all birds with name and count

# Print out the name and count of each bird


# 5) print per bird also the percentage of the total count

