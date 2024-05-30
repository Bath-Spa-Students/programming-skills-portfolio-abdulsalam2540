# Assign the person's name with whitespace characters
person_name = "\tAbdul Salam\n"

# Print the name with whitespace characters displayed
print("Original name with whitespace:")
print(f"'{Abdul Salam}'")

# Print the name using lstrip() to remove leading whitespace
print("\nName with leading whitespace removed using lstrip():")
print(f"'{Abdul Salam.lstrip()}'")

# Print the name using rstrip() to remove trailing whitespace
print("Name with trailing whitespace removed using rstrip():")
print(f"'{Abdul_Salam.rstrip()}'")

# Print the name using strip() to remove both leading and trailing whitespace
print("Name with leading and trailing whitespace removed using strip():")
print(f"'{Abdul_Salam.strip()}'")
