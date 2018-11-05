#Sorts the IDs of children in a family based on age
from addAge import addAge
from computeAge import computeAge
def us_28(listOfPeople, listOfFamilies):
     #listOfFamilies is a list of objects with Children, which is a list of people
     #for all families
    birthdayMap={}
    for people in listOfPeople:
        birthdayMap[people.ID]=people.Birthday
    for families in listOfFamilies:
        counter = 0
        if families.Children!="NA":
            currentChild=families.Children.split(",")
         #for all children in said family
            while(counter < len(currentChild)):
                x = counter
                currentBirthday = computeAge(birthdayMap[currentChild[counter]])
                #selection sort(?) for children in those families, based on age
                while (x > 0  and currentBirthday > computeAge(birthdayMap[currentChild[x-1]])):
                    temp = currentChild[x]
                    currentChild[x] = currentChild[x - 1]
                    currentChild[x-1] = temp
                    x = x - 1
                    
                counter = counter + 1
            print("LIST: In "+str(families.ID)+" Siblings order by decreasing age is: "+str(currentChild))
