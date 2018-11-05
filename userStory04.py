# Marriage should occur before divorce of spouses, and divorce can only occur after marriage
import change
def userStory04(listOfFamilies):
    flag = True
    for family in listOfFamilies:
        if family.Married != "NA":
            MarriedNum = change.changeDateToNum(family.Married)
            if family.Divorced != "NA":
                DivorcedNum = change.changeDateToNum(family.Divorced)
                if MarriedNum > DivorcedNum:
                    print("ERROR: FAMILY: US04: in " + family.ID + " Marriage occur after Divorce")
                    flag = False
        else:
            if family.Divorced != "NA":
                print("ERROR: FAMILY: US04: in " + family.ID + " Divorce occur with no Marriage")
    return flag
