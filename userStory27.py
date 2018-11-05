#Made by Mark Watson
#Fixes age for peoples whom have died

from computeAge import computeAge
def us_27(listOfPeople):
    

    for people in listOfPeople:
        if (people.Alive == False):
            people.Age = people.Age - computeAge(people.Death)
