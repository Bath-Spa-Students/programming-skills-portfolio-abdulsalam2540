# Make a list called sandwich_orders and fill it with the names of various sandwiches
sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'turkey', 'club', 'pastrami', 'roast beef', 'grilled cheese']

# Make an empty list called finished_sandwiches
finished_sandwiches = []

# Print a message saying the deli has run out of pastrami
print("Sorry, the deli has run out of pastrami.")

# Remove all occurrences of 'pastrami' from sandwich_orders using a while loop
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Loop through the list of sandwich orders
while sandwich_orders:
    # Remove the first sandwich order from the list and make the sandwich
    current_sandwich = sandwich_orders.pop(0)
    
    # Move the made sandwich to the list of finished sandwiches (excluding pastrami)
    if current_sandwich != 'pastrami':
        print(f"I made your {current_sandwich} sandwich.")
        finished_sandwiches.append(current_sandwich)

# Print a message listing each sandwich that was made (excluding pastrami)
print("\nSandwiches made:")
for sandwich in finished_sandwiches:
    print(sandwich.capitalize())
