'''Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.\
As they enter each topping, print a message saying you`ll add that topping to their pizza.'''

# Print a welcome message
print("Welcome to the Pizza Toppings Sprinkler!")

# Print instructions for the user 
print("Enter the names of a pizza topping or 'quit' to finish.")

# Start an infinite loop
while True:
    # Prompt the user to to enter a pizza topping
    topping = input("Please enter a topping:")

    # Check if the user entered 'quit'
    if topping.lower() == 'quit': 
        # If so, print a goodbye message 
        print("Thankyou for using the Pizza Toppings Sprinkler!")
        #And break the loop to end te program
        break
    else:
        # If the user entered something else, print a message saying that the topping will be added to the pizza.
        print(f"You will add {topping} to your pizza.")
