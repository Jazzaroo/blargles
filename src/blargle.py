'''Blargle 08 Jun 2011
@author Jasper Williams
'''
print("Welcome to the Blargle Generator, perhaps more famously known as the Blarglator.")
blarglist = []
class Blargle:#initial state of blargles
    mood = "calm"
    name = "blargie"
while True:
    user_choice = input("Please select an option from the following:\n"
                        "1) Create a Blargle.\n"
                        "2) Set the mood of a Blargle.\n"
                        "3) List, but do not alter Blargles.\n"
                        "4) Quit the Blarglator.\n")
    if user_choice == "1":
        new_blargle = Blargle()
        new_blargle.name = input("Please name the Blargle.\n")
        new_blargle.mood = input("How does %s feel today?\n" %new_blargle.name)
        blarglist.append(new_blargle)#adds new_blargle object to list blarglist
        print("%s is feeling %s." % (new_blargle.name, new_blargle.mood))#sanity check
    elif user_choice == "2":
        print("List of Blargles.\n")
        for x, a_blargle in enumerate(blarglist):#took a lot of trial; uses temp variable a_blargle as an integer to enumerate blarglist
            print("%d) %s is feeling %s." % (x, a_blargle.name, a_blargle.mood))
        user_pick = int(input("Select the number of the Blargle you would like to alter.\n"))
        blarglist[user_pick].mood = input("How does %s feel now?\n" % (blarglist[user_pick].name))
        print("%s is feeling %s." % (blarglist[user_pick].name, blarglist[user_pick].mood))
    elif user_choice == "3":
        print("List of Blargles.\n")
        for x, a_blargle in enumerate(blarglist):#same as in option 2, just does not lead to changes
            print ("%d) %s is feeling %s." % (x, a_blargle.name, a_blargle.mood))
    elif user_choice == "4":#quits the while loop, and the program by extension
        break
    else: 
        print( "Blargles cannot be made that way. ", user_choice, "! Really!\nTry again or exit the Blaglator.\n" )