# first method
# Assigning a name to the variable with whitespace and "\t", "\n" characters
name = "\t\n Manuel De Sa Jr\n\t"

# Printing the name with whitespace
print(f"Name with whitespace: '{name}'")

# Using lstrip() function to remove whitespace from the left side
name_lstrip = name.lstrip()
print(f"Name after lstrip(): '{name_lstrip}'")

# Using rstrip() function to remove whitespace from the right side
name_rstrip = name.rstrip()
print(f"Name after rstrip(): '{name_rstrip}'")

# Using strip() function to remove whitespace from both sides
name_strip = name.strip()
print(f"Name after strip(): '{name_strip}'")


# Second method
name = "\tManuel De Sa Jr\n"

# Print the name once, so the whitespace around the name is displayed
print("Original name:", name)

# Print the name using each of the three stripping functions
print("Name after lstrip():", name.lstrip())
print("Name after rstrip():", name.rstrip())
print("Name after strip(): name.strip()")
