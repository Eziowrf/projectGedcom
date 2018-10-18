def compareAge(date1, date2):
    age1 = date1.split('-')
    age2 = date2.split('-')
    ydiff = int(age2[0])-int(age1[0])
    if ydiff < 0: #compare date1 to date2, if date1 is before, return True
        return True
    elif ydiff == 0:
        mdiff = int(age2[1])-int(age1[1])
        if mdiff < 0:
            return True
        elif mdiff == 0:
            ddiff = int(age2[2])-int(age1[2])
            if ddiff < 0:
                return True
    else:
        return False
    
            
