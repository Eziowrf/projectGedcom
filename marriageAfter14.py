from compareAge import compareAge
from addAge import addAge
def marriageAfter14(listOfFamilies, listOfPeople):
    wife_birthday = []
    husband_birthday = []
    married = []
    husband = []
    wife = []
    for family in listOfFamilies:
        married = family.Married
        husband = family.HusbandID
        wife = family.WifeID
        for people in listOfPeople:
            if husband == people.ID:
                husband_birthday = people.Birthday
            if wife == people.ID:
                wife_birthday = people.Birthday
        husband_birthday = addAge(husband_birthday, '14-0-0')
        wife_birthday = addAge(wife_birthday, '14-0-0')

        if married != "NA":
            if compareAge(husband_birthday, married):
                print("ERROR: INDIVIDUAL: US10: " + family.HusbandID+ ": Husband married before age 14")
            if compareAge(wife_birthday, married):
                print("ERROR: INDIVIDUAL: US10: " + family.WifeID+ ": Wife married before age 14")

        
