def us_26(listOfFamilies, listOfPeople):
    result = True
    for people in listOfPeople:
        result_c = True
        result_s = True
        child_id = people.Child
        spouse_id = people.Spouse.split(",")
        if child_id != "NA":
            result_c = False
        if spouse_id[0] != "NA":
            result_s = False
            
        for family in listOfFamilies:
            if family.ID == child_id or family.ID in spouse_id:
                if people.ID in family.Children:
                    result_c = True
                if family.WifeID == people.ID or family.HusbandID == people.ID:
                    result_s = True
                    
            children_id = family.Children.split(",")
            if people.ID == family.HusbandID or people.ID == family.WifeID:
                if family.ID not in spouse_id:
                    print("ERROR: FAMILY: US26: " + family.ID+ ": Families information missing from individual")
                    result = False
            if people.ID in children_id:
                if family.ID != child_id:
                    print("ERROR: FAMILY: US26: " + family.ID+ ": Families information missing from individual")
                    result = False
                    
                
                    
                    
        if not result_c or not result_s:
                print("ERROR: INDIVIDUAL: US26: " + people.ID+ ": Individuals information missing from family")
                result = False

    return result

        
