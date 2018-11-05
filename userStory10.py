from compareAge import compareAge
from addAge import addAge
def us_10(listOfFamilies, listOfPeople):
    result = True
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
        if husband_birthday !="NA":
            husband_birthday = addAge(husband_birthday, '14-0-0')
        if wife_birthday !="NA":
            wife_birthday = addAge(wife_birthday, '14-0-0')

        if married != "NA":
            if compareAge(husband_birthday, married):
                print("ERROR: INDIVIDUAL: US10: " + family.HusbandID+ ": Husband married before age 14")
                result = False
            if compareAge(wife_birthday, married):
                print("ERROR: INDIVIDUAL: US10: " + family.WifeID+ ": Wife married before age 14")
                result = False
    return result

        
