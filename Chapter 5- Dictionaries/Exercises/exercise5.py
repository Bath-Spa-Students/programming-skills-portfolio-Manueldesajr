# Define several dictionaries for different pets
pet_1 = {"animal": "cat", "owner": "Lua"}
pet_2 = {"animal": "dog", "owner": "Mary"}
pet_3 = {"animal": "horse", "owner": "Matheuw"}

# Store these dictionaries in a list
pets = [pet_1, pet_2, pet_3]

# Loop through the list and print the information about each pet
for pet in pets:
    print(f"{pet['owner']} is the owner of a {pet['animal']}.")
