# Dates (birth, marriage, divorce, death) should not be after the current date, return True if no problems.
import time
from change import changeDateToNum 
def userStory01(listOfPeople, listOfFamilies):
    flag = True
    currentTimeList = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    currentTimeNum = changeDateToNum(currentTimeList)
    for people in listOfPeople:
        BirthdayNum = changeDateToNum(people.Birthday)
        DeathNum = changeDateToNum(people.Death)
        if BirthdayNum > currentTimeNum:
            print("ERROR: INDIVIDUAL: US01: " + people.ID + ": Birthday is after the current date")
            flag = False
        if DeathNum > currentTimeNum:
            print("ERROR: INDIVIDUAL: US01: " + people.ID + ": Death date is after the current date")
            flag = False
    for family in listOfFamilies:
        MarriedNum = changeDateToNum(family.Married)
        DivorcedNum = changeDateToNum(family.Divorced)
        if MarriedNum > currentTimeNum:
            print("ERROR: INDIVIDUAL: US01: " + people.ID + ": Married date is after the current date")
            flag =   False
        if DivorcedNum > currentTimeNum:
            print("ERROR: INDIVIDUAL: US01: " + people.ID + ": Divorced date is after the current date")
            flag = False
    return flag
