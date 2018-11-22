#Made by Mark Watson

#List all multiple births in a GEDCOM file (twins, triplets, etc.)
def us_32(listOfPeople, ListOfFamilies):


    listOfTwins = []

    for family in listOfFamilies:
    
        if family.Children != "NA":
            childList = family.Children.split(",")
            x = 0

        #for every child, if their birthday matches another, add them to the list

            while x < len(childList) - 1:
                y = x + 1

                while y < len(childList):
                    
                    birthday1 = "NA"
                    birthday2 = "NA"

                    #compares IDs to list of all people to get correct birthday from each child
                    for people in listOfPeople:

                        if childList[x] == people.ID:
                            birthday1 = people.Birthday
                        if childList[y] == people.ID:
                            birthday2 = people.Birthday
                            
                    if birthday1 == birthday2:
                        listOfTwins.append(childList[x])
                        listOfTwins.append(childList[y])

                    y = y + 1

                x = x + 1

        #removes duplicate IDs from list
        listOfTwins = list(set(listOfTwins))


    return listOfTwins
