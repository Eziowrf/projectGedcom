# Birth should occur before death of an individual
import change
def userStory03(listOfPeople):
    flag = True
    for people in listOfPeople:
        if people.Death != "NA":
            BirthdayNum = change.changeDateToNum(people.Birthday)
            DeathNum = change.changeDateToNum(people.Death)
            if BirthdayNum > DeathNum:
                print("ERROR: INDIVIDUAL: US03: Birthday of " + people.ID + " occur after Death")
                flag = False
    return flag

