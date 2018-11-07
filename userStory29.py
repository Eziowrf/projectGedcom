#Made by Mark Watson

#prints a list of dead people
def us_29(listOfPeople):

    deathList = [] 
    for people in listOfPeople:
        if people.Alive != True:
            deathList.append(people.Name)

    print(deathList)
