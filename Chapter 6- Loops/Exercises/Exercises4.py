# Make a list called sandwich_orders and fill it with the names of various sandwiches
sandwich_orders = ['tuna', 'turkey', 'club', 'roast beef', 'grilled cheese']

# Make an empty list called finished_sandwiches
finished_sandwiches = []

# Loop through the list of sandwich orders
while sandwich_orders:
    # Remove the first sandwich order from the list and make the sandwich
    current_sandwich = sandwich_orders.pop(0)
    print(f"I build your {current_sandwich} sandwich.")
    
    # Move the made sandwich to the list of finished sandwiches
    finished_sandwiches.append(current_sandwich)

# Print a message listing each sandwich that was made
print("\nSandwiches made:")
for sandwich in finished_sandwiches:
    print(sandwich.capitalize())
