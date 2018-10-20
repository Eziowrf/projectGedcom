#Made by Mark Watson
#Sorts the IDs of children in a family based on age

from addAge import addAge
from computeAge import computeAge
def us_28(listOfPeople, listOfFamilies):

    #listOfFamilies is a list of objects with Children, which is a list of people


    #for all families
    for families in listOfFamilies:
        counter = 0

        #for all children in said family
        while(counter < len(families.Children)):

            x = counter
            currentBirthday = computeAge(families.Children[counter].Birthday)

            #selection sort(?) for children in those families, based on age
            while (x > 0  and currentBirthday > computeAge(families.Children[x-1]):
                temp = families.Children[x]
                families.Children[x] = families.Children[x - 1]
                families.Children[x-1] = temp
                x = x - 1

            counter = counter + 1
