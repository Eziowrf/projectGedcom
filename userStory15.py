def us_15(listOfFamilies):
    flag = True
    for family in listOfFamilies:
        if family.Children != "NA":
            children = family.Children.split(',')
            
            if len(children) > 15:
                print("ERROR: FAMILY: US15: "+family.ID+": Family has more than 15 Children")
                flag = False
    return flag
