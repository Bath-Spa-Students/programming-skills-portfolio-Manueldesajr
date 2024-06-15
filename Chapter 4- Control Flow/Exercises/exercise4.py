'''
•If the person is less than 2 years old, print a message that the person is a baby.
•If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
•If the person is at least 4 years old but less than 13, print a message that the person is a kid.
•If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
•If the person is at least 20 years old but less than 65, print a message that the person is an adult.
•If the person is age 65 or older, print a message that the person is an elder.'''

# Set a value for the variable age (ex: age = 25), OR take the age as an Input from the user.

# Get the age from the user
age = int(input("Enter the age: "))

# Write an if-elif-else chain that determines a person`s stage of life.
if age < 2:
    print("The person id a Baby.")
elif age < 4:
    print("The person is a Toddler.")
elif age < 13:
    print("The person is a Kid.")
elif age < 20:
    print("The person is a Teenager.")
elif age < 65:
    print("The person is an Adult.")
else:
    print("The person is an Elder.")
