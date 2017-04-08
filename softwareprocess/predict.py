import math
import datetime
import re
import StarsTable

def Predict(values):
    if 'body' not in values:
        values['error'] = 'Mandatory information is missing'
        return values
    if 'lat' in values:
        values['error'] = 'Latitude is invalid'
        return values
    if 'long' in values:
        values['error'] = 'Longitude is invalid'
        return values

    if 'date' not in values:
        values['date'] = '2001-01-01'
    if 'date' in values:
        date = values['date'].split('-')
        if not len(date) == 3:
            values['error'] = 'date is invalid'
            return values
        #check 'year' valid or not
        year = date[0]
        if int(year) < 2001:
            values['error'] = 'date is invalid'
            return values
        if not year.isdigit() or len(year) != 4:
            values['error'] = 'date is invalid'
            return values
        year = int(year)
        #check 'month' valid or not
        month = date[1]
        if not len(month) == 2:
            values['error'] = 'date is invalid'
            return values
        if not month.isdigit() or int(month) > 12 or int(month) < 0:
            values['error'] = 'date is invalid'
            return values
        month = int(month)
        #check 'day' valid or not
        day = (date[2])
        if not day.isdigit() or not len(day) == 2:
            values['error'] = 'date is invalid'
            return values
        day = int(day)
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if day != 31:
                values['error'] = 'date is invalid'
                return values
        if month == 2 and year % 4 == 0:     #check leap year
            if day != 29:
                values['error'] = 'date is invalid'
                return values
        if month == 02 and year % 4 == 0:
            if not day == 28:
                values['error'] = 'date is invalid'
                return values
        if month == 4 or month == 6 or month == 9 or month == 11:
            if not day == 30:
                values['error'] = 'date is invalid'
                return values

    if 'time' not in values:
        values['time'] = '00:00:00'
    if 'time' in values:
        time = values['time'].split(':')
        if not len(time) == 3:
            values['error'] = 'time is invalid'
            return values
        # check hour valid or not
        hour = time[0]
        if not hour.isdigit() or not len(hour) == 2:
            values['error'] = 'time is invalid'
            return values
        hour = int(hour)
        if hour >= 24 or hour < 0:
            values['error'] = 'time is invalid'
            return values
        # check minutes valid or not
        minute = time[1]
        if not minute.isdigit() or  not len(minute) == 2:
            values['error'] = 'time is invalid'
            return values
        minute = int(minute)
        if minute >= 60 or minute < 0:
            values['error'] = 'time is invalid'
            return values
        # check second valid or not
        second = time[2]
        if not second.isdigit() or not len(second) == 2:
            values['error'] = 'time is invalid'
            return values
        second = int(second)
        if second >= 60 or second < 0:
            values['error'] = 'time is invalid'
            return values

    starName = values['body'][0].upper() + values['body'][1:].lower()
    if starName not in StarsTable.stars:
        values['error'] = 'star not in catalog'
        return values
    newStar = StarsTable.getStar[starName].split(',')


    #getStar = read_file(values['body'])
    #if (getStar == -1):
     #   values['error'] = "star not in catalog"
      #  return values

    GHA = '100d42.6'
    SHA = newStar[0]
    latitude = newStar[1]
    #SHA = getStar[1]
    #latitude = getStar[2]
    gapYear = year - 2001
    diffAngular = gapYear * degreeToMinute('-0d14.31667')
    countLeapYear = gapYear / 4
    dailyRotation = abs(degreeToMinute('360d0.00') - (86164.1/86400) * degreeToMinute('360d00.0'))
    totalPro = dailyRotation * countLeapYear
    nowGHA = degreeToMinute(GHA) + diffAngular + totalPro
    totalSecond1 = second + minute * 60 + hour * 3600
    epoch = datetime(year, 1, 1)
    now = datetime(year, month, day)
    totalSecond2 = (now - epoch).total_second
    totalSecond = totalSecond1 + totalSecond2
    countRotation = totalSecond / (86164.1) * degreeToMinute('360d00.0')
    newGHA = nowGHA + countRotation
    starGHA = newGHA + degreeToMinute(SHA)
    newStarGHA = minuteToDegree(starGHA)
    values['long'] = newStarGHA
    values['lat'] = latitude
    return values

"""
def read_file(star):
    filePath = os.path.dirname(__file__)
    Stars = open(filePath + '/stars.txt')
    for i in range(0, 60):
        line = Stars.readline()
        newLine = line.split()
        if (newLine[0].lower() == star.lower()):
            return newLine
    Stars.close()
    return -1
"""


def degreeToMinute(d):
    degree = d.split('d')
    hour = int(degree[0])
    minute = float(degree[1])
    if hour != 0:
        if hour > 0:
            newDegree = hour + minute/60
        else:
            newDegree = hour - minute/60
    else:
        newDegree = abs(minute/60)
    return newDegree

def minuteToDegree(m):
    degree = str(m).split('.')
    hour = int(degree[0])
    minute = (m - hour) * 60
    newm = str(hour) + 'd' +str(minute)
    return newm



def isLeapYear(s):
    if s % 4 != 0:
        return -1

def totalDays(m, y):
    if isLeapYear(y) != -1:
        if m == 1:
            return 0
        if m == 2:
            return 31
        if m == 3:
            return 31 + 29
        if m == 4:
            return 31 + 29 + 31
        if m == 5:
            return 31 + 29 + 31 + 30
        if m == 6:
            return 31 + 29 + 31 + 30 + 31
        if m == 7:
            return 31 + 29 + 31 + 30 + 31 + 30
        if m == 8:
            return 31 + 29 + 31 + 30 + 31 + 30 + 31
        if m == 9:
            return 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31
        if m == 10:
            return 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30
        if m == 11:
            return 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
        if m == 12:
            return 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 +30

    if isLeapYear(y) == -1:
        if m == 1:
            return 0
        if m == 2:
            return 31
        if m == 3:
            return 31 + 28
        if m == 4:
            return 31 + 28 + 31
        if m == 5:
            return 31 + 28 + 31 + 30
        if m == 6:
            return 31 + 28 + 31 + 30 + 31
        if m == 7:
            return 31 + 28 + 31 + 30 + 31 + 30
        if m == 8:
            return 31 + 28 + 31 + 30 + 31 + 30 + 31
        if m == 9:
            return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31
        if m == 10:
            return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30
        if m == 11:
            return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
        if m == 12:
            return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 +30

