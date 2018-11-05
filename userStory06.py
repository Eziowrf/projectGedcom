# Divorce can only occur before death of both spouses
def userStory06(listOfPeople, listOfFamilies):
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
        if family.Divorced != "NA":
            DivorcedNum = changeDateToNum(family.Divorced)
            people_wife = findPeopleByID(family.WifeID)
            people_husband = findPeopleByID(family.HusbandID)
            DeathNumOfWife = changeDateToNum(people_wife.Death)
            DeathNumOfHusband = changeDateToNum(people_husband.Death)
            if DeathNumOfHusband < DivorcedNum:
                print("ERROR: FAMILY: US06: " + family.ID + ": Divorce occur after death of husband " + people_husband.ID)
                flag = False
            if DeathNumOfWife < DivorcedNum:
                print("ERROR: FAMILY: US06: " + family.ID + ": Divorce occur after death of wife " + people_wife.ID)
                flag = False
    return flag