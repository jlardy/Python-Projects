""" 
This is a simple program that I made to create a gift exchange for a family that has restraints on who can have who.

Definitely not an efficient solution but it works for something slapped together.

Make a person class for each person you want to be in the exchange then run the program 

Each member is stored in a list fam. 

A random assignment is made for each person until everyone has been assigned. People can't get anyone in their "can't have" list. 
"""

import random

fam = []
class person:
    def __init__(self, name, cant_have):
        self.name = name
        self.cant_have = cant_have
        self.beenAssigned = False
        self.assigned = None
        fam.append(self)

# add people here, names have to be the spelled the same
person('Sib1', [])
person('Sib2', [])
person('Mom', ['Dad'])
person('Dad', ['Mom'])


def assign():
    counter = 0
    for person in fam:
        counter = 0
        choice = fam[random.randint(0, len(fam)-1)]
       
        while choice.name == person.name or choice.beenAssigned or choice.name in person.cant_have:
            choice = fam[random.randint(0, len(fam)-1)]
            counter += 1
            # error handling, if the last person in the group hasnt been assigned anyone and cant be assigned anyone that is available, then the program calls itself again 
            if counter > 1000:
                for i in fam:
                    i.beenAssigned = False
                random.shuffle(fam)
                return assign()

        choice.beenAssigned = True
        person.assigned = choice.name

assign()
for person in fam:
    print('[', person.name,',' ,person.assigned, ']')


