# Death should be less than 150 years after birth for dead people,
# and current date should be less than 150 years after birth for all living people
import time
def userStory07(listOfPeople):
    flag = True
    def changeDateToNum(date):  # date format must be like "2018-10-06"
        if date == "NA":
            return 0
        else:
            tempDate = date.split('-')
            return int(tempDate[0] + tempDate[1] + tempDate[2])
    for people in listOfPeople:
        if people.Death != "NA" and people.Birthday != "NA":
            BirthdayNum = changeDateToNum(people.Birthday)
            DeathNum = changeDateToNum(people.Death)
            if DeathNum - BirthdayNum >= 1500000:
                print("ERROR: INDIVIDUAL: US07: death should be less than 150 years after birth for " + people.ID)
                flag = False
        if people.Death == "NA" and people.Birthday != "NA":
            BirthdayNum = changeDateToNum(people.Birthday)
            currentDate = changeDateToNum(time.strftime('%Y-%m-%d', time.localtime(time.time())))
            if currentDate - BirthdayNum >= 1500000:
                print("ERROR: INDIVIDUAL: US07: current date should be less than 150 years after birth for " + people.ID)
                flag = False
    return flag