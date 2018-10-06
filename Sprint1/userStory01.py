import  time
# Dates (birth, marriage, divorce, death) should not be after the current date, return True if no problems.
def userStory01(listOfPeople, listOfFamilies):
    def changeDateToNum(date): # date format must be like "2018-10-06"
        if date == "NA":
            return 0 # 0 will not larger than any date
        else:
            tempDate = date.split('-')
            return int(tempDate[0] + tempDate[1] + tempDate[2])

    currentTimeList = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    currentTimeNum = changeDateToNum(currentTimeList)
    for people in listOfPeople:
        BirthdayNum = changeDateToNum(people.Birthday)
        DeathNum = changeDateToNum(people.Death)
        if BirthdayNum > currentTimeNum:
            return False
        if DeathNum > currentTimeNum:
            return False
    for family in listOfFamilies:
        MarriedNum = changeDateToNum(family.Married)
        DivorcedNum = changeDateToNum(family.Divorced)
        if MarriedNum > currentTimeNum:
            return False
        if DivorcedNum > currentTimeNum:
            return False
    return True