import math
import StarsTable
import datetime

def Predict(values):
    if 'body' not in values:
        values['error'] = 'Mandatory information is missing'
        return values

    starName = values['body'][0].upper() + values['body'][1:].lower()
    if starName not in StarsTable.stars:
        values['error'] = 'star not in catalog'
        return values
    star = StarsTable.getStar(starName).split(',')
    GHA = '100d42.6'
    SHA = star[0]
    latitude = star[1]

    if 'lat' in values:
        values['error'] = 'Latitude is invalid'
        return values
    if 'long' in values:
        values['error'] = 'Longitude is invalid'
        return values

    if 'date' not in values:
        values['date'] = '2001-01-01'
    else:
        date = values['date'].split('-')
        if len(date) != 3:
            values['error'] = 'date is invalid'
            return values
        if checkDate(date) == -1:
            values['error'] = 'date is invalid'
            return values

    if 'time' not in values:
        values['time'] = '00:00:00'
    else:
        time = values['time'].split(':')
        if not len(time) == 3:
            values['error'] = 'time is invalid'
            return values
        if checkTime(time) == -1:
            values['error'] = 'time is invalid'
            return values

    years = int(date[0])
    months = int(date[1])
    days = int(date[2])
    hours = int(time[0])
    minutes = int(time[1])
    seconds = int(time[2])
    # Determine angular difference for each year
    gapYear = years - 2001
    diffAngular = gapYear * degreeToMinute('-0d14.31667')
    # Take into account leap years
    countLeapYear = int(gapYear / 4)
    dailyRotation = abs(degreeToMinute('360d0.00') - (86164.1/86400) * degreeToMinute('360d00.0'))
    totalPro = dailyRotation * countLeapYear
    # Calculate GHA(2016-01-01)
    nowGHA = degreeToMinute(GHA) + diffAngular + totalPro
    # Calculate the angle (include total second)
    totalSecond1 = seconds + minutes * 60 + hours * 3600
    epoch = datetime(years, 1, 1)
    now = datetime(years, months, days)
    totalSecond2 = (now - epoch).total_seconds() * 86400
    totalSecond = totalSecond1 + totalSecond2
    countRotation = totalSecond / (86164.1) * degreeToMinute('360d00.0')
    # Calculate total GHA(2016-01-17)
    newGHA = nowGHA + countRotation
    # Calculate the star's GHA
    starGHA = newGHA + degreeToMinute(SHA)
    newStarGHA = minuteToDegree(starGHA)
    values['long'] = newStarGHA
    values['lat'] = latitude
    return values


def checkDate(dates):
    year = dates[0]    #check year
    if not year.isdigit() or len(year) != 4:
        return -1
    if int(year) < 2001:
        return -1
    month = dates[1]   #check month
    if not month.isdigit() or len(month) != 2:
        return -1
    if int(month) <= 0 or int(month) > 12:
        return -1
    day = dates[2]     #check day
    if not day.isdigit() or len(day) != 2:
        return -1
    day = int(day)
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day != 31:
           return -1
    if month == 2 and year % 4 == 0:     #check leap year
        if day != 29:
            return -1
    if month == 02 and year % 4 == 0:
        if day != 28:
            return -1
    if month == 4 or month == 6 or month == 9 or month == 11:
        if day != 30:
            return -1

def checkTime(times):
    hour = times[0]      #check hour
    if not hour.isdigit() or len(hour) != 2:
        return -1
    if int(hour) >= 24 or int(hour) < 0:
        return -1
    minute = times[1]    #check minute
    if not minute.isdigit() or len(minute) != 2:
        return -1
    if int(minute) >= 60 or int(minute) < 0:
        return -1
    second = times[2]    #check second
    if not second.isdigit() or len(second) != 2:
        return -1
    if int(second) >= 60 or int(second) < 0:
        return -1

def degreeToMinute(n):
    degree = n.split('d')
    hour = int(degree[0])
    minute = float(degree[1])
    if hour != 0:
        if hour < 0:
            newDegree = -1 * (abs(hour) + minute / 60)
    newDegree = hour + minute / 60
    return newDegree

def minuteToDegree(m):
    degree = math.floor(m)
    if m < 0:
       degree = math.ceil(m)
    redegree = degree * 360
    minute = abs(round((m - degree) * 60, 1))
    newDegree = '%dd%.1f' % (redegree, minute)
    return newDegree
"""
    degree = str(m).split('.')
    hour = int(degree[0])
    minute = (m - hour) * 60
    newm = str(hour) + 'd' +str(minute)
    return newm
"""
