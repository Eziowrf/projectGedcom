def userStory02(listOfPeople, listOfFamilies):
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
            BirthdayNumOfWife = changeDateToNum(findPeopleByID(family.WifeID).Birthday)
            if BirthdayNumOfWife > MarriedNum:
                return False
            BirthdayNumOfHusband = changeDateToNum(findPeopleByID(family.HusbandID).Birthday)
            if BirthdayNumOfHusband > MarriedNum:
                return False
    return True