def us_24(listOfPeople,listOfFamily):
    res=True
    spouseObj=[]
    spouseList=[]
    familyList=[]
    marrigeDateList=[]
    for family in listOfFamily:
        spouseObj.append(family.HusbandID)
        spouseObj.append(family.WifeID)
        spouseList.append(spouseObj)
        spouseObj=[]
        familyList.append(family.ID)
        marrigeDateList.append(family.Married)
    for i in range(len(spouseList)):
        j=i+1
        while j<len(spouseList):
            inter = list(set(spouseList[i]).intersection(set(spouseList[j])))
            if len(inter)>=2:
                if marrigeDateList[i]==marrigeDateList[j] and marrigeDateList!="NA":
                    print("ERROR: FAMILY: US24: "+familyList[i]+" and "+familyList[j]+"  have same Spouse Name and Married date: "+marrigeDateList[i])
                    res=False
            j=j+1
    return res