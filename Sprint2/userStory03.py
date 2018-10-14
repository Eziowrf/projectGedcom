# Birth should occur before death of an individual
def userStory03(listOfPeople):
    flag = True
    def changeDateToNum(date):  # date format must be like "2018-10-06"
        if date == "NA":
            return 0  # 0 will not larger than any date, for later comparison
        else:
            tempDate = date.split('-')
            return int(tempDate[0] + tempDate[1] + tempDate[2])
    for people in listOfPeople:
        if people.Death != "NA":
            BirthdayNum = changeDateToNum(people.Birthday)
            DeathNum = changeDateToNum(people.Death)
            if BirthdayNum > DeathNum:
                print("ERROR: INDIVIDUAL: US03: Birthday of " + people.ID + " occur after Death")
                flag = False
    return flag

