# timer module using datetime

import datetime

startTime = None
endTime = None
elapsed = []
time = "time elapsed: None"

def formatTime(timeVar):
    timestr = str(timeVar)
    timeList = []
    timeList.append(int(timestr[:4]))
    timeList.append(int(timeVar.strftime("%j")))
    timeList.append(int(timestr[11:13]))
    timeList.append(int(timestr[14:16]))
    timeList.append(float(timestr[17:]))
    return timeList

def timeDiff(start, end):
    times = {
        0:0,
        1:365,
        2:24,
        3:60,
        4:60
    }
    diff = []
    for i in range(len(start)):
        diff.append(end[i] - start[i])
    for i in range(len(diff)-1,-1,-1):
        if diff[i] < 0:
            diff[i] += times[i]
            diff[i-1] = diff[i-1] - 1
            if i == 1 and start[0]%4 == 0:
                diff[i] += 1
    return diff

def startTimer():
    global startTime, endTime
    startTime = datetime.datetime.now()
    endTime = None

def endTimer():
    global startTime, endTime, elapsed, time
    endTime = datetime.datetime.now()
    time = "time elapsed: "
    if type(startTime) == None: startTime = endTime
    elapsed = timeDiff(formatTime(startTime),formatTime(endTime))
    times = {
        0:" year",
        1:" day",
        2:" hour",
        3:" minute",
        4:" second"
    }
    for i in range(len(elapsed)):
        if elapsed[i] == 0: continue
        time += str(elapsed[i]) + times[i]
        if elapsed[i] != 1: time+="s "
        else: time+=" "


def printTime():
    global time
    print(time)

