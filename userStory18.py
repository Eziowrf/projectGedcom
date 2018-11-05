# User Story 17: Siblings should not marry

def US_18(listOfPeople):
    groupMap={}
    for people in listOfPeople:
        sp=people.Spouse.split(",")
        #print(sp)
        if people.Child not in groupMap and people.Child != "NA":
            groupMap[people.Child]=[]
            for obj in sp:
                groupMap[people.Child].append(obj)
        elif people.Child in groupMap:
            for obj1 in sp:
                if obj1!='NA':
                    groupMap[people.Child].append(obj1)
    #print(groupMap)
    for value in groupMap.values():
        #print(value)
        for i in value:
            if value.count(i)!=1:
                print("ERROR: FAMILY: US18: in family"+" "+i+" "+"has married their sibilings")
                a= False
                break
            else:
                a= True
    
    return a 
