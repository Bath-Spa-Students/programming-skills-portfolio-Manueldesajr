# Write a loop that never ends, and run it. (To end the loop, press ctrl-C or close the window displaying the output.)

# Start an infinite loop
while True:
    # Print a message instructing how to break the infinite loop
    print("This loop is a never-ending party! To sneak out, press Ctrl+C. Dont worry, the loop won`t take it personally!")

    # Prompt the user from the input 
    user_input = input(" 'quit' to exit the loop: ")
    
    # Check if the user wants to quit the loop 
    if user_input.lower() == 'quit':
        # If so, break out of the loop
        break
