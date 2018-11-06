def us_22(listOfPeople,listOfFamilies):
    map_pid={}
    map_fid={}
    a=True
    b=True
    for I1 in listOfPeople:
        if I1.ID not in map_pid:
            map_pid[I1.ID]=1
        else:
            map_pid[I1.ID]=map_pid[I1.ID]+1
    for I2 in listOfFamilies:
        if I2.ID not in map_fid:
            map_fid[I2.ID]=1
        else:
            map_fid[I2.ID]=map_fid[I2.ID]+1
    for y in map_pid:
        if map_pid[y]>1:
            print("ERROR: INDIVIDUAL: US22: There are  "+str(map_pid[y])+" same individual ID: "+y)
            a = False
    for x in map_fid:
        if map_fid[x]>1:
            print("ERROR: FAMILY: US22: There are  "+str(map_fid[x])+" same family ID: "+x)
            b=False

    return a and b