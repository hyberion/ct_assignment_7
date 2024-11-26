#Task 2- User Input Data Processor
#WWrite a script that asks for and checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.
#We do as we are commanded.  The Warp awaits for those who fail to be vigilant
#Those who are not enthusiastic will be reported and adjusted accordingly

#First Version



#We check the length of the first name and last name and make sure they are at least 2 characters long.  Because only a heretic would have a name
#that short.  And we must be vigilant against the heretics.
# We set this up so that if either the first name or last name is less or equal to 2 characters long, the user is suspected of heresy and must report to the nearest Inquisitorial office for questioning.
# We can not allow even the smallest hint of zenos heracy to go unchecked.  The Emperor Protects
# We use a function for this because to be effecient is the Emperors will

def is_valid_name(name, min_length=3):
    return len(name) >= min_length and name.isalpha()

#We ask for the user's first name
first_name = input("What is your first name? ").strip()
#We ask for the user's last name
last_name = input("What is your last name? ").strip()

if not is_valid_name(first_name):
    print("Error: First must be at least 2 characters long and contain only letters. \n You are suspected of heresy.  Please report to the nearest Inquisitorial office for questioning.")
elif not is_valid_name(last_name):
    print("Error: Last must be at least 2 characters long and contain only letters. \n You are suspected of heresy.  Please report to the nearest Inquisitorial office for questioning.")   
else:
    print(f"Hello, {first_name} {last_name}.  You are not suspected of heresy.  For now.")


#We have completed this stalward ballwark against the zenos threat.
#Hail the Omnisiah.  The Emperor Protects