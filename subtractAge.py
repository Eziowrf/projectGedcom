def subtractAge(date, time):
    age = date.split('-')
    change = time.split('-')
    if int(age[2]) >= int(change[2]):
        age[2] = int(age[2])-int(change[2])
    else:
        change[1] = int(change[1])+1
        if age[1] in {"01", "03", "05", "07", "08", "10", "12"}:
            age[2] = int(age[2])+31-int(change[2])
        elif age[1] in {"04", "06", "09", "11"}:
            age[2] = int(age[2])+30-int(change[2])
        elif age[1] == "02":
            age[2] = int(age[2])+28-int(change[2])
            
    if int(age[1]) >= int(change[1]):
        age[1] = int(age[1])-int(change[1])
    else:
        change[0] = int(change[0])+1
        age[1] = int(age[1])+12-int(change[1])

    age[0] = int(age[0])-int(change[0])

    return str(age[0])+'-'+str(age[1])+'-'+str(age[2])
