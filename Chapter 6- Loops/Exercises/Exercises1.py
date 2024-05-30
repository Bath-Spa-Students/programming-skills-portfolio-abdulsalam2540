# Initialize an empty list to store toppings
toppings = []

# Prompt the user to enter toppings until they enter 'quit'
while True:
    topping = input("Enter a pizza topping (enter 'quit' to finish): ").lower()
    
    if topping == 'quit':
        break
    
    # Add the topping to the list
    toppings.append(topping)
    
    # Print a message confirming the addition of the topping
    print(f"Adding {topping} to your pizza.")

# Print the final list of toppings
print("Your pizza will have the following toppings:")
print(', '.join(toppings))
