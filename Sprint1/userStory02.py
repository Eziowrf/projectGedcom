# Birth should occur before marriage of an individual
def userStory02(listOfPeople, listOfFamilies):
    flag=True
    def changeDateToNum(date):  # date format must be like "2018-10-06"
        if date == "NA":
            return 0  # 0 will not larger than any date
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
            BirthdayNumOfWife = changeDateToNum(people_wife.Birthday)
            BirthdayNumOfHusband = changeDateToNum(people_husband.Birthday)
            if BirthdayNumOfWife > MarriedNum:
                print("ERROR: FAMILY: US02: " + family.ID + ": Wife's birthday occurs after Marriage date")
                flag= False
            if BirthdayNumOfHusband > MarriedNum:
                print("ERROR: FAMILY: US02: " + family.ID + ": Husband's birthday occurs after Marriage date")
                flag= False
    return flag
