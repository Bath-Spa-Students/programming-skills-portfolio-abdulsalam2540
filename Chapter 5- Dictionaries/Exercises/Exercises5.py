# Create dictionaries for different pets
pet1 = {'animal': 'dog', 'owner': 'Alice'}
pet2 = {'animal': 'cat', 'owner': 'Bob'}
pet3 = {'animal': 'parrot', 'owner': 'Charlie'}

# Store the dictionaries in a list called pets
pets = [pet1, pet2, pet3]

# Loop through the list and print information about each pet
for pet in pets:
    print(f"{pet['owner'].capitalize()}'s pet is a {pet['animal']}.")
