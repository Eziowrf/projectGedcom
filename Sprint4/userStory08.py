# Children should be born after marriage of parents (and not more than 9 months after their divorce)
def userStory08(listOfPeople, listOfFamilies):
    flag = True
    def changeDateToNum(date):  # date format must be like "2018-10-06"
        if date == "NA":
            return 0
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
            if family.Children != "NA":
                for id in family.Children.split(','):
                    child = findPeopleByID(id)
                    if child.Birthday != "NA":
                        BirthdayNum = changeDateToNum(child.Birthday)
                        if MarriedNum > BirthdayNum:
                            print("ERROR: FAMILY: US08: In family " + family.ID + ", birthday of child " + id + " is before parents' marriage")
                            flag = False
        if family.Divorced != "NA":
            DivorcedNum = changeDateToNum(family.Divorced)
            if family.Children != "NA":
                for id in family.Children.split(','):
                    child = findPeopleByID(id)
                    if child.Birthday != "NA":
                        BirthdayNum = changeDateToNum(child.Birthday)
                        if DivorcedNum // 100 % 10 < 4:
                            BirthdayNum = BirthdayNum - 900
                        else:
                            BirthdayNum = BirthdayNum - 9700
                        if BirthdayNum > DivorcedNum:
                            print("ERROR: FAMILY: US08: In family " + family.ID + ", birthday of child " + id + " is more than 9 months after parents' divorce")
                            flag = False
    return flag