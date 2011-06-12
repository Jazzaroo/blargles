'''Blargle 08 Jun 2011
@author Jasper Williams
'''
import random
import time

def CreateBlargle(blarglist):
    new_blargle = Blargle()
    new_blargle.name = input("Please name the Blargle.\n")
    new_blargle.mood = input("How does %s feel today?\n" %new_blargle.name)
    blarglist.append(new_blargle)#adds new_blargle object to list blarglist
    print("%s is feeling %s." % (new_blargle.name, new_blargle.mood))#sanity check

def BlargGen (blarglist, blarg):
    new_blargle = Blargle()
    new_blargle.name = blarg.babyname
    new_blargle.mood = "calm"
    blarglist.append(new_blargle)
    blarg.babyname = ""
    blarg.randiness = 0
    print("A new Blargle has been born! Welcome to life, %s, childe of %s." % (new_blargle.name, blarg.name))
    
def try_Knockboots(blarglist, blarg):
    print("%s is getting randy! Is someone else feeling the same?" % (blarg.name))
    for a_blarg in blarglist:
        if a_blarg.babyname == "" and a_blarg.randiness >= 6 and a_blarg.name != blarg.name: #cause pregos can't get randy and we don't want Blargles to self-seed
            blargdad = a_blarg.name
            partner = True # boot-knocking to commence shortly
            break
        else: 
            partner = False # no boot-knocking will occur
    if partner == True:
        print("Hot damn! %s got lucky with %s!" % (blarg.name, blargdad))
        print("We're having a baby!")
        blarg.babyname = blargdad[:random.randint(1,3)] + blarg.name[random.randint(1,3):]
        blarg.randiness = 0
        return blargdad
    if partner == False:
        print("No, it seems not.")

def DisplayBlargles(blarglist):
    print ("List of Blargles.\n")
    for x, a_blargle in enumerate(blarglist):
        print ("%d) %s is feeling %s." % (x, a_blargle.name, a_blargle.mood))

def DispBlargles(blarglist):
    print("%d Blargles remain in the world." % (len(blarglist)))
    for x, a_blargle in enumerate(blarglist):
        print ("%d) %s" % (x+1, a_blargle.name))

def BlargLife(blarglist):
    for index, blarg in enumerate(blarglist):
        if blarg.babyname != "":
            BlargGen(blarglist, blarg)
        if blarg.randiness >= 12:
            try_Knockboots(blarglist, blarg)
        blarg.randiness += random.randint(0,3)
        if blarg.hunger >= 10:
            Consume(blarglist, index, blarg)
            Reap(blarglist)
        blarg.hunger += random.randint(0,3)

def Reap(blarglist):
    toreap = []
    for a_blarg in blarglist:
        if a_blarg.life == False:
            print("The Ferryman has taken %s to the Underworld." % a_blarg.name)
            toreap.append(a_blarg)
    for victim in toreap:
        blarglist.remove(victim)
                
def Consume(blarglist, index, blarg):
    print("%s is getting hungry." % (blarg.name))
    if len(blarglist) > 1:
        winner = random.randint(0, len(blarglist)-1) #chooses a lucky blargle for being eaten
        while winner == index:
            winner = random.randint(0, len(blarglist)-1)
        print("Chomp! %s ate %s!" % (blarg.name, blarglist[winner].name))
        blarglist[winner].life = False
        blarg.hunger = 0
    elif len(blarglist) == 1:
        print("The last Blargle, %s, has died of starvation!" % blarg.name)
        blarg.life = False

def check_civstatus(blarglist):
    if len(blarglist) == 0:
        print("All of the Blargles have lived their short, violent lives and have passed away into oblivion.")    
          
class Blargle:#initial state of blargles
    mood = ""
    name = ""
    randiness = 5
    hunger = 0
    babyname = "" ##used to be prego flag
    life = True
    def __init__(self, newname = "blargie", newmood = "calm"):
        self.name = newname
        self.mood = newmood


day = 1

print("Welcome to the Blargle Generator, perhaps more famously known as the Blarglator.")
blarglist = [ Blargle("John", "angry"), Blargle("Susan", "calm"),
              Blargle("William", "stupid"), Blargle("Jessie", "irradiated"),
              Blargle("Markos", "peeved"), Blargle("Angela", "livid") ]

while True:
    user_choice = input("Please select an option from the following:\n"
                        "1) Create a Blargle.\n"
                        "2) Set the mood of a Blargle.\n"
                        "3) List, but do not alter Blargles.\n"
                        "4) Quit to simulation of Blargle life.\n")
    if user_choice == "1":
        CreateBlargle(blarglist)
    elif user_choice == "2":
        DisplayBlargles(blarglist)
        while True:
            try:
                user_pick = int(input("Select the number of the Blargle you would like to alter.\n"))
                blarglist[user_pick].mood = input("How does %s feel now?\n" % (blarglist[user_pick].name))
                break
            except ValueError:
                print("That's crazy! Try again.")
            except:
                print("Invalid selection. Try again.")
        print("%s is feeling %s." % (blarglist[user_pick].name, blarglist[user_pick].mood))
    elif user_choice == "3":
        DisplayBlargles(blarglist)
    elif user_choice == "4":#quits the while loop, and the program by extension
        break
    else: 
        print("Blargles cannot be made that way. ", user_choice, "! Really!\nTry again or exit the Blaglator.\n")

#Now we run Blargles through their paces
while len(blarglist)>0:
    print("Day %d. Another great day to be a Blargle!" % (day))
    DispBlargles(blarglist)
    time.sleep(3) #causes a delay before day gets rolling
    BlargLife(blarglist) #everything that happens to Blargles, happens here
    check_civstatus(blarglist) #if there are no more Blargles, it declares the end
    day += 1 #increments the day
    time.sleep(3) #causes a delay before next day