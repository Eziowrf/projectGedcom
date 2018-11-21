def us_16(listOfFamilies, listOfPeople):
    flag = True
    for family in listOfFamilies:
        count = 0
        family_name = []
        if family.HusbandName != "NA":
            family_name = family.HusbandName.split('/')[1]
        
        if family.Children != "NA":
            children = family.Children.split(',')
            for child in children:
                for people in listOfPeople:
                    if child == people.ID:
                        names = people.Name.split('/')
                        if names[1] != family_name and people.Gender == "M":
                            print("ERROR: FAMILY: US16: "+family.ID+": Family has male child " + child + " with different last name")
                            flag = False
    return flag
