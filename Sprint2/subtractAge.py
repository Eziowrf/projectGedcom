def subtractAge(date, time):
    age = date.split('-')
    change = time.split('-')
    if age[1] > change[1]:
        age[1] = int(age[1])-int(change[1])
    else:
        change[0] = int(change[0])+1
        age[1] = int(age[1])+12-int(change[1])

    age[0] = int(age[0])-int(change[0])

    return str(age[0])+'-'+str(age[1])+'-'+str(age[2])
