def us_20(listOfPeople,listOfFamily):
    flag=True
    spouseObj=[]
    grandparent=[]
    childMap={}
    grandparentMap={} 
    parentMap={}
    spouseMap={} 
    
    for people in listOfPeople:
        childMap[people.ID]=people.Child
    #print(childMap)
    for family in listOfFamily:
        spouseObj.append(family.WifeID)
        spouseObj.append(family.HusbandID)
        spouseMap[family.ID]=spouseObj
        spouseObj=[]

    for eachFamily in spouseMap:
        #print(eachFamily)
        for spouses in spouseMap[eachFamily]:
            if spouses!="NA" and spouses in childMap:
                if childMap[spouses]=="NA":
                    parentMap[spouses]=["NA"]
                else:
                    parentMap[spouses]=spouseMap[childMap[spouses]]

    #print (parentMap)
    for eachParents in parentMap:
        for parents in parentMap[eachParents]:
            #print(parents)
            if parents!="NA":
                if childMap[parents]=="NA":
                    continue
                else:
                    for eachGrandParent in spouseMap[childMap[parents]]:
                        grandparent.append(eachGrandParent)  
        grandparentMap[eachParents]=grandparent
        grandparent=[]
    
    for eachSpouse in listOfFamily:
        if eachSpouse.WifeID!="NA" and eachSpouse.HusbandID!="NA":
            result=(determin(parentMap[eachSpouse.WifeID],grandparentMap[eachSpouse.HusbandID]) or determin(parentMap[eachSpouse.HusbandID],grandparentMap[eachSpouse.WifeID]))
            if result==True:
                print("ERROR: FAMILY: US19: In family"+" "+eachSpouse.ID+" "+"has married between aunt and uncle with nieces and nephews")
                flag=False

    print(flag)
    return flag

def determin(list1, list2): 
    result = False
    # traverse in the 1st list 
    for x in list1: 

        # traverse in the 2nd list 
        for y in list2: 
    
            # if one common 
            if x == y: 
                result = True
                return result  
                
    return result 





    