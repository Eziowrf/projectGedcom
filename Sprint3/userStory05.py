# Marriage should occur before death of either spouse
def userStory05(listOfPeople, listOfFamilies):
    flag = True
    def changeDateToNum(date):  # date format must be like "2018-10-06"
        if date == "NA":
            return 9999999999  # this number will not less than any date, for later comparison
        else:
            tempDate = date.split('-')
            return int(tempDate[0] + tempDate[1] + tempDate[2])
    def findPeopleByID(ID):
        for people in listOfPeople:
            if people.ID == ID:
                return people
        return False
    for family in listOfFamilies:
        if family.Married != "NA":
            MarriedNum = changeDateToNum(family.Married)
            people_wife = findPeopleByID(family.WifeID)
            people_husband = findPeopleByID(family.HusbandID)
            DeathNumOfWife = changeDateToNum(people_wife.Death)
            DeathNumOfHusband = changeDateToNum(people_husband.Death)
            if DeathNumOfWife < MarriedNum:
                print("ERROR: FAMILY: US05: " + family.ID + ": Marriage occur after death of wife " + people_wife.ID)
                flag = False
            if DeathNumOfHusband < MarriedNum:
                print("ERROR: FAMILY: US05: " + family.ID + ": Marriage occur after death of husband " + people_husband.ID)
                flag = False
    return flag
