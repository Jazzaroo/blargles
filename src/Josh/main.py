'''
Created on Jun 11, 2011

@author: Joshua
'''
from Blargle import *
import random
import time
import sys
       

def EatRandomBlargle( eater, blargles ):
    if len(blargles) > 1:
        to_kill = eater;
        while to_kill == eater:
            to_kill = random.randint( 0, len( blargles ) - 1 )
            
        print ( "Sweet JESUS! %s ate %s! The humanity!" % (blargles[eater].name, blargles[to_kill].name) )
        del blargles[to_kill]
        return True
    else:
        return False

def TryReproduce( parent_index, blargles ):
    if len(blargles) > 1:
        to_special_hug = parent_index;
        while to_special_hug == parent_index:
            to_special_hug = random.randint( 0, len( blargles ) - 1 )
        print ( "Whoa - %s just reproduced with %s to make a new Blargle!" %
                    (blargles[parent_index].name, blargles[to_special_hug].name ) )
        
        blargles.append( Blargle( ( blargles[parent_index], blargles[to_special_hug]) ) )
            
    
def BlargleIsAlive( ablargle ):
    return ablargle.state != BLARGLE_STATES.DEAD
    
def PrintBlargles( blargles, year ):
    #C.B.E. is Common Blargle Era
    print ("------========Blargle Civilizaton %d C.B.E.========------" % year )
    for a_blargle in blargles:
        sys.stdout.write ("Blargle " + a_blargle.name )
        if a_blargle.generation == 2:
            sys.stdout.write (" the 2nd" )
        elif a_blargle.generation == 3:
            sys.stdout.write (" the 3rd")
        elif a_blargle.generation > 3:
            sys.stdout.write( " the %dth" % a_blargle.generation)
            
        print(", hunger:%d" %  a_blargle.hunger )
    print ("")
    
if __name__ == '__main__':
    blargles = [ Blargle("Sally"), Blargle("Thomas"),
                Blargle("Arcturious"), Blargle("Stanley"),
                Blargle("Jehosephat"), Blargle("Eminem"),
                Blargle("Brosephalus")]
    # Create initial state - a list of Blargles
    while True:
        choice = input( "(c)reate a blargle, or (r)un: " ).lower()
        try:
            if choice == "c":
                aBlargle = Blargle()
                aBlargle.name = input( "Name:")
                blargles.append(aBlargle)
            elif choice == "r":
                break
            else:
                raise Exception("Bad choice")
        except Exception as e:
            print( "Invalid (%s); please try again.\n" % e )
    
        
    # Critical loop, for each blargle, pass, eat, or grave
    year = 0
    while len(blargles) > 0 :
        year += 1
        for index, a_blargle in enumerate(blargles):
            if a_blargle.state == BLARGLE_STATES.DEAD:
                continue
            if a_blargle.state == BLARGLE_STATES.ALIVE:
                a_blargle.hunger += 1
                if random.randint( 0, ABSTINENCE_COMMITMENT) == ABSTINENCE_COMMITMENT:
                    TryReproduce( index, blargles )
            if a_blargle.hunger >= HUNGER_TO_EAT and a_blargle.hunger < HUNGER_TO_DIE:
                if random.randint(0, 5 ) > 3 and EatRandomBlargle( index, blargles ):
                    a_blargle.hunger = 0
            elif a_blargle.hunger >= HUNGER_TO_DIE:
                print ("Blargle %s died of hunger." % a_blargle.name )
                a_blargle.state = BLARGLE_STATES.DEAD
        blargles = list(filter(BlargleIsAlive, blargles))
        PrintBlargles( blargles, year )
        time.sleep(1)
        
    print( "\n***END OF BLARGLE SPECIES***")
                