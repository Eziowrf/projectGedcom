
# User Story 17: No marriages to descendants


def US_17(listOfPeople):

    for people in listOfPeople:
        sp=people.Spouse.split(",")
        #print(sp)
        if people.Child in sp:
            a= False
            if a==False:
                print("Error! US17:"+people.ID+" "+"has married with child")
                break
        else:
            #print("not in this line")
            a=True
    return a