def changeDateToNum(date): # date format must be like "2018-10-06"
    if date == "NA":
        return 0 # 0 will not larger than any date
    else:
        tempDate = date.split('-')
        return int(tempDate[0] + tempDate[1].zfill(2) + tempDate[2].zfill(2))
