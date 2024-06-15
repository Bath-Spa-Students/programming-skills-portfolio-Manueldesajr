# Write three strings in different variables and print the output as one string.
def concatenate_strings(str1, str2, str3):
    # Concatenate and return the strings
    return str1 + " " + str2 + " " + str3

# Define the strings as parts of a joke
string1 = "Why don't scientists trust atoms?"
string2 = "Because they"
string3 = "make up everything!"

# Call the function with the strings as arguments
print(concatenate_strings(string1, string2, string3))
