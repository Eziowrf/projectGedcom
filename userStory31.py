#Made by Mark Watson

#List all living people over 30 who have never been married in a GEDCOM file
def us_31(listOfPeople):

    singleList = []

    for people in listOfPeople:
        if people.Spouse == "NA" and int(people.Age) > 30:

            singleList.append(people.Name)

    print("This is a list of living people over 30 who have not married: " +str(singleList))
