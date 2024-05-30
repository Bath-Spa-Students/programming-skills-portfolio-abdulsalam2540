# Dictionary containing three major rivers and the country each river runs through
rivers = {
    'nile': 'Egypt',
    'amazon': 'Brazil',
    'yangtze': 'China'
}

# Print a sentence about each river
print("Rivers and the countries they run through:")
for river, country in rivers.items():
    print(f"The {river.capitalize()} runs through {country}.")

# Print the name of each river included in the dictionary
print("\nNames of rivers:")
for river in rivers.keys():
    print(river.capitalize())

# Print the name of each country included in the dictionary
print("\nNames of countries:")
for country in rivers.values():
    print(country)
