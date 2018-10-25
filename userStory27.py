#Made by Mark Watson
#Fixes age for peoples whom have died

from addAge import addAge
from computeAge import computeAge
def us_27(listOfPeople, listOfFamilies):
    

    for people in listOfPeople:
        if (Alive == False):
            people.Age = people.Age - computeAge(people.Death)
