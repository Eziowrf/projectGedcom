from addAge import addAge
from computeAge import computeAge
def us_12(listOfFamilies, listOfPeople):
    flag = True
    for family in listOfFamilies:
        children_birthdays = []
        father_birthday = []
        mother_birthday = []
        if family.Children != "NA":
            children = family.Children.split(',')
            for child in children:
                for people in listOfPeople:
                    if child == people.ID:
                        children_birthdays.append(people.Birthday)

        for people in listOfPeople:
            if family.WifeID == people.ID:
                if people.Birthday != "NA":
                    mother_birthday = people.Birthday
            if family.HusbandID == people.ID:
                if people.Birthday != "NA":
                    father_birthday = people.Birthday
                    
        if children_birthdays != []:
            for child in children_birthdays:
                if mother_birthday != []:
                    motherAge = addAge(mother_birthday, "60-0-0")
                    if computeAge(child) < computeAge(motherAge):
                        print("ERROR: INDIVIDUAL: US12: "+family.WifeID+": Mother more than 60 years older than child of Birthday " + child)
                        flag = False
                if father_birthday != []:
                    fatherAge = addAge(father_birthday, "80-0-0")
                    if computeAge(child) < computeAge(fatherAge):
                        print("ERROR: INDIVIDUAL: US12: "+family.HusbandID+": Father more than 80 years older than child of Birthday "+child)
                        flag = False
        
    return flag
