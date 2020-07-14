import time
shipName = "Gloss"
captain = "Captain Joon "
location = "Andromeda Galaxy"
password = "Syubie"

pAttempt = input("Enter the password: ")
while pAttempt != password:
    print ("Password incorrect")
    pAttempt = input("Enter the password: ")
print ("Password correct. Welcome to " + shipName)

print ("")
print ("The spaceship " + shipName + " is currently visiting " + location + ".")

choice = ""
while choice != "/exit":
    print ("What would you like to do, " + captain + "?")
    print ("")
    print ("a. Travel to another galaxy")
    print ("b. Fire thrusters")
    print ("c. Open the airlock")
    print ("d. Self-destruct")
    print ("/exit to exit")
    print ("")
    choice = input ("Enter your choice: ")

if choice == "a":
    destination = input("Where would you like to go? ")
    print ("Leaving" + location)
    print ("Travelling to " + destinationtime.sleep(5))
    print ("Arrived at " + destination)
    location = desination
