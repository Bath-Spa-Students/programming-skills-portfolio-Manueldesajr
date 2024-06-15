'''A girl heads to a computer shop to buy some USB sticks.\
She loves USB sticks and wants as many as she can get for £50. They are £6 each.
Write a programme that calculates how many USB sticks she can buy and\
how many pounds she will have left.'''

# Define the cost of a USB stick
cost_per_usb = 6
# Get the amount of money the girl has to spend
budget = 50

# Calculate the number of USB sticks she can buy
number_of_usb = budget // cost_per_usb

# Calculate the amount of money she will have left
money_left = budget % cost_per_usb

# Print the results
print("The girl can buy", number_of_usb, "USB sticks.")
print("She will have", money_left, "pounds left.")
