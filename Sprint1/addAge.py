def addAge(date, time):
    age = date.split('-')
    change = time.split('-')
    if int(age[1]) + int(change[1]) > 12:
        age[1] = int(age[1]) + int(change[1]) - 12
        change[0] = int(change[0])+1
    else:
        age[1] = int(age[1])+int(change[1])

    age[0] = int(age[0])+int(change[0])

    return str(age[0])+'-'+str(age[1])+'-'+str(age[2])
