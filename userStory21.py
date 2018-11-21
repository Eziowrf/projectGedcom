def us_21(listOfPeople,listOfFamily):
    husbandMap={}
    wifeMap={}
    genderMap={}
    result=True
    for people in listOfPeople:
        genderMap[people.ID]=people.Gender
    for family in listOfFamily:
        if family.HusbandID!="NA" and family.WifeID!="NA":
            husbandMap[family.ID]=family.HusbandID
            wifeMap[family.ID]=family.WifeID
    for eachHusband in husbandMap:
        if genderMap[husbandMap[eachHusband]]!="M":
            print("ERROR: FAMILY: US21: In family"+" "+eachHusband+" "+"Husband's gender is not Male")
            result=False

    for eachWife in wifeMap:
        if genderMap[wifeMap[eachWife]]!="F":
            print("ERROR: FAMILY: US21: In family"+" "+eachWife+" "+"Wife's gender is not Female")
            result=False
    return result