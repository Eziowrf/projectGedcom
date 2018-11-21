def us_23(listOfPeople,listOfFamily):
    res=True
    peopleInfo={}
    peopleInfoDupli={}
    Idstr=""
    for people in listOfPeople:
        peopleInfo[people.ID]=people.Name+","+people.Birthday
    for k,v in peopleInfo.items():
        if v in peopleInfoDupli:
            peopleInfoDupli[v].append(k)
        else:
            peopleInfoDupli[v]=[]
            peopleInfoDupli[v].append(k)
    for nameAndBirth in peopleInfoDupli:
        if len(peopleInfoDupli[nameAndBirth])>=2:
            for Id in peopleInfoDupli[nameAndBirth]:
                Idstr=Idstr+Id+" "
            print("ERROR: INDIVIDUAL: US23: "+Idstr+" have same individual Name and Birthday")
            res=False
    return res
        