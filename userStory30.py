#Made by Mark Watson

#Prints a list of married alive people
def us_30(listOfPeople):

    marriedList = [] 

    for people in listOfPeople:
        if people.Spouse != "NA" and people.Alive == True:

            marriedList.append(people.Name)

    print(marriedList)
