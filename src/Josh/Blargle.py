'''
Created on Jun 11, 2011

@author: Joshua
'''
ABSTINENCE_COMMITMENT = 5
HUNGER_TO_EAT = 3
HUNGER_TO_DIE = 6
import random

class BLARGLE_STATES:
    ALIVE=1
    DEAD=2

class Blargle:
    name = ""
    hunger = 0
    generation = 1
    state = BLARGLE_STATES.ALIVE
    def __init__(self, C = "name"):
        if isinstance(C, tuple):
            mom, dad = C
            self.name = mom.name[:random.randint(3,len(mom.name))]
            self.name += dad.name[random.randint(3,len(dad.name)):]
            self.generation = max( mom.generation, dad.generation) + 1
        elif isinstance( C, str):
            self.name = C
            
    