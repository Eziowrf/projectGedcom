import time
def computeAge(Fdate):
    timeList = Fdate.split('-')
    currentTimeList = time.strftime('%Y-%m-%d', time.localtime(time.time())).split('-')
    tempAge = int(currentTimeList[0]) - int(timeList[0])
    if int(currentTimeList[1]+ currentTimeList[2]) - int(timeList[1]+ timeList[2]) >= 0:
        return tempAge
    else:
        return tempAge - 1