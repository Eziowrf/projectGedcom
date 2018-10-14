# Marriage should occur before divorce of spouses, and divorce can only occur after marriage
def userStory04(listOfFamilies):
    flag = True
    def changeDateToNum(date):  # date format must be like "2018-10-06"
        if date == "NA":
            return 0  # 0 will not larger than any date, for later comparison
        else:
            tempDate = date.split('-')
            return int(tempDate[0] + tempDate[1] + tempDate[2])

    for family in listOfFamilies:
        if family.Married != "NA":
            MarriedNum = changeDateToNum(family.Married)
            if family.Divorced != "NA":
                DivorcedNum = changeDateToNum(family.Divorced)
                if MarriedNum > DivorcedNum:
                    print("ERROR: FAMILY: US04: in " + family.ID + " Marriage occur after Divorce")
                    flag = False
        else:
            if family.Divorced != "NA":
                print("ERROR: FAMILY: US04: in " + family.ID + " Divorce occur with no Marriage")
    return flag