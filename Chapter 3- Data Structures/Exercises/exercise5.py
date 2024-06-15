'''You just heard that one of your guests can`t make the
dinner, so you need to send out a new set of invitations. You`ll have to think of
someone else to invite.
•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can `t make it.
•Modify your list, replacing the name of the guest who can`t make it with the name of the new person you are inviting.
•Print a second set of invitation messages, one for each person who is still in your list.'''

# List of people invited to dinner
guests = ["Manuel","Eva", " Diana", "Amelia Earhart",\
          "Youseff", "Mary"]

# Print an invitation message for each person
for guest in guests:
    print(f"Dear {guest}, you are kindly invited to join me for a dinner of intellectual conversation \
and good food. Looking forward to your presence.")
    
# Name of guest who can`t make it 
absent_guest = "Frank"
print(f"\nUnfortunately, {absent_guest} can`t make it to the dinner.\n")

# Replace the absent guest with a new guest
new_guest = " Amini"
guests[guests.index(absent_guest)] = new_guest

# Print a new set of invitation messages
for guest in guests:
    print(f"Dear {guest}, you are kindly invited to join me for a dinner of intellectual conversation \
and good food. Looking forward to your presence.")
