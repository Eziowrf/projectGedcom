import change
def us_11(listOfFamilies):
    flag = True
    for family in listOfFamilies:
        
        if family.Married != "NA":
            marriageValue = change.changeDateToNum(family.Married)
            wifeID = family.WifeID
            husbandID = family.HusbandID
            divorceDate = family.Divorced
            for family2 in listOfFamilies:
                if ((wifeID == family2.WifeID and husbandID != family2.HusbandID) or (husbandID == family2.HusbandID and wifeID != family2.WifeID)) and family2.Married != "NA":
                    marriage2Value = change.changeDateToNum(family2.Married)
                    if family2.Divorced == "NA" and marriage2Value < marriageValue:
                        print("ERROR: FAMILY: US11: Spouse married twice at the same time in families " + family.ID + " and " + family2.ID)
                        flag = False
                    elif divorceDate == "NA" and marriage2Value > marriageValue:
                        print("ERROR: FAMILY: US11: Spouse married twice at the same time in families " + family.ID + " and " + family2.ID)
                        flag = False
                    elif family2.Divorced != "NA":
                        divorced2Value = change.changeDateToNum(family2.Divorced)
                        if divorced2Value > marriageValue:
                            print("ERROR: FAMILY: US11: Spouse married twice at the same time in families " + family.ID + " and " + family2.ID)
                            flag = False
                    elif divorceDate != "NA":
                        divorcedValue = change.changeDateToNum(divorceDate)
                        if divorcedValue > marriage2Value:
                            print("ERROR: FAMILY: US11: Spouse married twice at the same time in families " + family.ID + " and " + family2.ID)
                            falg = False
    return flag
                            
