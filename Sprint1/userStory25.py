# No more than one child with the same name and birth date should appear in a family
def userStory25(listOfPeople, listOfFamilies):
    flag=True
    def findPeopleByID(ID):
        for people in listOfPeople:
            if people.ID == ID:
                return people
        return False
    def isInList(NB, listOfNB): # NB means name and birth
        for nb in listOfNB:
            if nb == NB:
                return True
        return False

    for family in listOfFamilies:
        listofNB = []
        if len(family.Children.split(',')) > 1: # family.Children is like "I1,I2,I3"
            for id in family.Children.split(','):
                recentPerson = findPeopleByID(id)
                if recentPerson !=False:
                    NB = recentPerson.Name + '-' + recentPerson.Birthday
                    if not isInList(NB, listofNB):
                        listofNB.append(NB)
                    else:
                        print("ERROR: FAMILY: US25: " + family.ID + ": Child " + id + " in this family has repeated name and birthday")
                        flag= False
    return flag
