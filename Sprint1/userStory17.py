
# User Story 17: No marriages to descendants


def US_17(listOfPeople,listOfFamily):

    for people in listOfPeople:
        sp=people.Spouse.split(",")
        #print(sp)
        if people.Child in sp and people.Child != "NA":
            a= False
            if a==False:
                print("ERROR: INDIVIDUAL: US17: "+people.ID+": "+"has married with child")
        else:
            #print("not in this line")
            a=True
    for family in listOfFamily:
        childID=family.Children.split(",")
        if family.WifeID in childID and family.WifeID != "NA":
            print("ERROR: INDIVIDUAL: US17: "+family.WifeID+": "+"has married with child")
            a=False
        elif family.HusbandID in childID and family.HusbandID != "NA":
            print("ERROR: INDIVIDUAL: US17: "+family.HusbandID+": "+"has married with child")
            a=False
    return a
