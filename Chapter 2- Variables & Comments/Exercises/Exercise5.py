# Constants
usb_Amount = 10  # Price of each USB stick in pounds
total_money = 50  # Total money the girl has in pounds

# Calculate the number of USB sticks she can buy
num_usb_sticks = total_money // usb_Amount

# Calculate the remaining money after buying USB sticks
remaining_money = total_money % usb_Amount

# Print the results
print("Number of USB sticks she can buy:", num_usb_sticks)
print("Pounds left after buying USB sticks:", remaining_money)
