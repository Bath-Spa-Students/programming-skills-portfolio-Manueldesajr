# Deduction of the current guest list, only two people invited due to space constraints.

# List of people invited to dinner
guests = ["Manuel","Lorden", "Tome", "Amelia",\
          " Yousafzai", " Frank"]

# Print an invitation message for each person
for guest in guests:
    print(f"Dear {guest}, you are kindly invited to join me for a dinner of intellectual conversation \
and good food. Looking forward to your presence.")
    
# Name of guest who can`t make it 
absent_guest = "Anne "
print(f"\nUnfortunately, {absent_guest} can`t make it to the dinner.\n")

# Replace the absent guest with a new guest
new_guest = "Amini"
guests[guests.index(absent_guest)] = new_guest

# Print a new set of invitation messages
for guest in guests:
    print(f"Dear {guest}, you are kindly invited to join me for a dinner of intellectual conversation \
and good food. Looking forward to your presence.")

# Start of Ex:6   
# Print a message about the new dining table
print("\nI just found out that the new dining table won`t arrive in time for the dinner,\
      and I have space for only two guests\n")

# Remove guests from the list until only two remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(
        f"Dear {removed_guest}, I`m sorry to inform you that I can`t invite you to the dinner\
          due to space constraints.")
    
# Print a message to the remaining guests
for guest in guests:
    print(f"\nDear {guest}, despite the change in plans, you are still invited to the dinner.")

# Remove the last two names from the list
del guests[:]

# Print the list to make sure it`s empty.
print("\nFinal guest list:", guests)
